# sequential-evalue-ledger

## Français

Suivre une preuve séquentielle sans transformer chaque arrêt en test fixe.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m sequential_evalue_ledger examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Construit un e-processus classique par rapport de vraisemblance mélange bêta/binomial, en espace logarithmique. Conserve le premier franchissement de 1/alpha, même si la valeur redescend ensuite.

### Limites

Validité conditionnelle au modèle nul Bernoulli p0, prior et test fixés ; ne corrige pas des données sélectionnées ou plusieurs essais non déclarés. Calcul flottant, pas nouvelle preuve statistique ni conseil d’investissement.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Track sequential evidence without treating every stopping point as a fixed test.

Synthetic data; no network access or secret required.

```sh
python -m sequential_evalue_ledger examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Builds a classical beta/binomial mixture likelihood-ratio e-process in log space. Keeps the first crossing of1/alpha even when the value later declines.

### Limits

Validity assumes the conditional Bernoulli p0 null and fixed prior/test; does not correct selected data or undeclared multiple tests. Floating-point calculation, no new statistical proof or investment advice.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Seguir evidencia secuencial sin tratar cada parada como prueba fija.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m sequential_evalue_ledger examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Construye e-proceso clásico por razón de verosimilitud mezcla beta/binomial en espacio logarítmico. Conserva primer cruce de1/alpha aunque luego descienda.

### Límites

Validez bajo nulo Bernoulli p0 condicional y prior/prueba fijos; no corrige selección de datos o múltiples pruebas ocultas. Cálculo flotante, sin nueva prueba estadística ni consejo de inversión.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://arxiv.org/abs/1808.03204
