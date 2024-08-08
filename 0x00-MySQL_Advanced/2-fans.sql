/* best band ever */

USE DATABASE holberton;
SELECT origin, SUM(fans) as nb_fans FROM metal_bands GROUP BY origin ORDERED BY nb_fans;
