from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import os

import matplotlib
matplotlib.use('Agg')  
app = Flask(__name__)

# Suppression des valeurs manquantes pour éviter des erreurs dans les analyses
def load_and_clean_data():
    file_path = 'data/cinemas.csv'  
    df = pd.read_csv(file_path, sep=';')

   
    df_long = pd.melt(df, 
                      id_vars=['commune', 'population de la commune', 'écrans', 'fauteuils'], 
                      value_vars=[col for col in df.columns if col.startswith('entrées')],
                      var_name='annee',
                      value_name='entrees_annuelles')
    
    
    df_long['annee'] = df_long['annee'].str.extract(r'(\d+)').astype(int)

    
    df_long.rename(columns={
        'population de la commune': 'population_commune',
        'écrans': 'ecrans',
        'fauteuils': 'fauteuils'
    }, inplace=True)

    
    df_long.dropna(inplace=True)

    return df_long



@app.route('/')
def index():
    df = load_and_clean_data()

    # Étape 1 
    stats = df[['fauteuils', 'ecrans', 'entrees_annuelles']].describe().to_html(classes='table table-striped')

    df.head(10).plot(kind='bar', x='commune', y='entrees_annuelles', color='skyblue')
    plt.title('Top 10 Entrées Années 2022')
    plt.xlabel('Commune')
    plt.ylabel('Entrées annuelles')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    plt.savefig('static/images/exploration_top10.png')
    plt.close()

    # Étape 2 
    df['entrees_par_fauteuil'] = df['entrees_annuelles'] / df['fauteuils']
    top_10_communes = df.groupby('commune')['entrees_par_fauteuil'].mean().sort_values(ascending=False).head(10)
    top_10_communes.plot(kind='bar', color='green', edgecolor='black')
    plt.title('Top 10 Communes - Entrées Moyennes par Fauteuil')
    plt.xlabel('Commune')
    plt.ylabel('Entrées Moyennes par Fauteuil')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('static/images/top10_fauteuils.png')
    plt.close()

    meilleures_communes = df.groupby('commune')['entrees_par_fauteuil'].mean().sort_values(ascending=False).head(3).to_dict()
    pires_communes = df.groupby('commune')['entrees_par_fauteuil'].mean().sort_values(ascending=True).head(3).to_dict()

    # Étape 3 
    corr_ecrans = df['ecrans'].corr(df['entrees_annuelles'])
    corr_fauteuils = df['fauteuils'].corr(df['entrees_annuelles'])
    sns.lmplot(x='ecrans', y='entrees_annuelles', data=df, height=6)
    plt.title('Corrélation entre Écrans et Entrées Annuelles')
    plt.savefig('static/images/correlation_ecrans.png')
    plt.close()
    sns.lmplot(x='fauteuils', y='entrees_annuelles', data=df, height=6)
    plt.title('Corrélation entre Fauteuils et Entrées Annuelles')
    plt.savefig('static/images/correlation_fauteuils.png')
    plt.close()

    
    conclusion_corr = "Le nombre d'écrans semble avoir un impact légèrement plus important que le nombre de fauteuils sur les entrées annuelles, selon les coefficients de corrélation."

  
    # Étape 4 
    df_train = df[df['annee'] < 2022]
    df_test = df[df['annee'] == 2022]

    X_train = df_train[['ecrans', 'fauteuils', 'population_commune']]
    y_train = df_train['entrees_annuelles']
    X_test = df_test[['ecrans', 'fauteuils', 'population_commune']]
    y_test = df_test['entrees_annuelles']

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)




    # Étape 5 
    commune_fictive = [[2, 120, 20000]]
    prediction = model.predict(commune_fictive)[0]

    
    strategie = "Augmenter légèrement le nombre d'écrans semble être une stratégie efficace pour cette commune fictive, car le nombre d'écrans a une corrélation plus élevée avec les entrées annuelles."

    return render_template('index.html', stats=stats, 
                           image_path='static/images/exploration_top10.png',
                           image_path1='static/images/top10_fauteuils.png',
                           corr_ecrans=corr_ecrans, 
                           corr_fauteuils=corr_fauteuils,
                           image_path2='static/images/correlation_ecrans.png',
                           image_path3='static/images/correlation_fauteuils.png',
                           r2=r2, mae=mae, prediction=prediction, 
                           meilleures_communes=meilleures_communes,
                           pires_communes=pires_communes,
                           conclusion_corr=conclusion_corr, 
                           strategie=strategie)

if __name__ == '__main__':
    print("Le serveur Flask est en cours d'exécution...")
    app.run(debug=True, port=5001)
