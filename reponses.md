3. Le répertoire `.github/workflows` est utilisé par GitHub Actions pour stocker les fichiers de définition de workflow. Ca décrit tous les processus à automatisers qui vont s'executer à l'apparition d'événements spécifiques.

8. On observe une nouvelle exécution du workflow. Cette exécution apparaît dans la liste des workflows, indiquant son statut, le commit et la branche concernés. En cliquant dessus, on peut visualiser les détails de chaque job et les logs des étapes exécutées.


10. On constate qu'un nouveau workflow nommé "Run Tests" a été déclenché. L'événement `push` a initié cette exécution.

11. Après avoir modifié `model.py` pour introduire un bug, le prochain `git push` déclenchera à nouveau le workflow "Run Tests". Lors de l'exécution de `pytest`, les tests qui vérifient la sortie "positive" pour la fonction `predict_sentiment` échoueront car la fonction retourne maintenant "positif". L'échec des tests entraînera un code de sortie non nul pour la commande `pytest`, ce qui fera échouer l'étape "Run tests" et par conséquent l'ensemble du workflow "Run Tests".

12. En corrigeant le bug dans `model.py`, le code est correct et correspond à ce que les tests vérifient, la commande `pytest` s'exécute sans erreur et termine avec un code de sortie 0. Par conséquent, l'étape "Run tests" réussit, et l'ensemble du workflow "Run Tests" est marqué comme succès.

13. Le prochain `git push` déclenchera le workflow "Run Tests". Cette fois, au lieu d'un seul job "test", GitHub Actions lancera trois jobs en parallèle sous le nom "test" : "test (3.8)", "test (3.9)", et "test (3.10)". Chaque job configurera la version de Python spécifiée par la matrice et exécutera les étapes indépendamment. Cela permet de vérifier la compatibilité et le bon fonctionnement du code sur plusieurs environnements Python simultanément.

14. Après avoir poussé le commit contenant la modification du workflow pour utiliser une matrice Python, on observe dans l'onglet "Actions" que le workflow "Run Tests" a été déclenché. Au lieu d'un seul job "test", on voit maintenant trois jobs s'exécuter en parallèle : "test (3.8)", "test (3.9)", et "test (3.10)". Chaque job exécute les mêmes étapes définies dans le fichier YAML mais avec la version de Python correspondante spécifiée dans la matrice. Le statut global du workflow ne sera marqué comme succès que si les trois jobs réussissent individuellement.

15. Un nouveau workflow `.github/workflows/lint.yml` est créé pour exécuter `flake8` avec des options spécifiques (`--select=E9,F63,F7,F82`). Ce workflow se déclenche également sur `push` et `pull_request`.

16. On observe dans l'onglet "Actions" que les deux workflows ("Run Tests" et "Lint Code") sont déclenchés. Le workflow "Run Tests" devrait réussir comme précédemment. Le workflow "Lint Code" devrait également réussir, car les vérifications `flake8` configurées ne concernent pas la présence ou le style des docstrings, mais plutôt des erreurs de syntaxe, des noms non définis, etc. L'ajout de docstrings valides ne viole pas ces règles spécifiques.

18.Dès l'ouverture de la PR, le workflow "PR Comment" (`pr-comment.yml`) est déclenché par l'événement `pull_request: opened`. Il exécute son job qui utilise `actions/github-script` pour poster automatiquement un commentaire sur la page de la PR avec le message "👋 Thanks for the PR! The automated tests will run shortly.".

20. Permet d'afficher un badge sur le readme affichant le statut du workflow

24. On observe dans l'onglet "Actions" que le workflow "Docker Build" exécute les étapes de construction et de test de l'image Docker.


