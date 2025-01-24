# Math Exercise Project

This project consists of mathematical exercises involving matrix operations and transformations in 3D space, specifically focusing on matrix multiplication and rotation in the RGB color space.

## Project Structure

```
math-exercise
├── src
│   ├── main.py
│   ├── matrix_multiplication.py
│   ├── rotation_matrix.py
│   └── transformations.py
├── requirements.txt
└── README.md
```

## Files Description

- **src/matrix_multiplication.py**: Contains a function that multiplies two matrices:
  - Matrix A: [[1, 2, 3], [4, 5, 6]]
  - Matrix B: [[10, 11], [13, 14], [16, 17]]
  
- **src/rotation_matrix.py**: Defines a function to calculate the rotation matrix for rotating around the line D1 that passes through the points (0,0,0) and (255,255,255) in R3.

- **src/transformations.py**: Includes functions that perform a second transformation to ensure that colors remain within the RGB cube after rotation. It also provides the mathematical representation of this transformation.

- **src/main.py**: the file you can tweak to test and run the examples.

## Requirements

To run this project, you need to install the following dependencies:

- numpy

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## How to Run the Code

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies.
4. Run the scripts in the `src` folder to perform the matrix multiplication and transformations.

## Mathematical Concepts

# **Matrix Multiplication**: The process of multiplying two matrices to produce a third matrix.
# Multiplication Matricielle

Cet exercise explore la multiplication matricielle, un concept clé en mathématiques et informatique. Voici un exemple détaillé, accompagné d'une implémentation Python.

---

## Données Initiales

Nous avons deux matrices :

- **Matrice `A`** (taille `2x3`) :
  ```plaintext
  A =
  [ 1  2  3 ]
  [ 4  5  6 ]
- **Matrice `B`** (taille `3x2`) :
  ```plaintext
  B =
  [ 10  11 ]
  [ 13  14 ]
  [ 16  17 ]
- La multiplication de `A` et `B` donne une nouvelle matrice `C`, de taille `2x2`. Chaque élément de `C` est calculé en prenant le produit scalaire d'une ligne de `A` et d'une colonne de `B`. Voici les calculs détaillés :
  ```plaintext
  C[1,1] = (1 * 10) + (2 * 13) + (3 * 16) = 10 + 26 + 48 = 84
  C[1,2] = (1 * 11) + (2 * 14) + (3 * 17) = 11 + 28 + 51 = 90
  C[2,1] = (4 * 10) + (5 * 13) + (6 * 16) = 40 + 65 + 96 = 201
  C[2,2] = (4 * 11) + (5 * 14) + (6 * 17) = 44 + 70 + 102 = 216

## Résultat

- **La matrice résultante `C`** (taille `2x2`) :
  ```plaintext
  C =
  [  84   90 ]
  [ 201  216 ]

# **Rotation Matrix**: A matrix that is used to perform a rotation in Euclidean space.


## Matrice de Rotation dans $$\( \mathbb{R}^3 \)$$ autour de la droite $$\( D1 \)$$

La droite $$\( D1 \)$$ passe par les points $$\( (0, 0, 0) \)$$ et $$\( (255, 255, 255) \)$$. Nous voulons effectuer une rotation autour de cette droite. Voici les étapes pour calculer la matrice de rotation.

---

### 1. Définition du vecteur directeur

Le vecteur directeur de $$\( D1 \)$$ est donné par :

$$
\vec{u} = \frac{(255, 255, 255)}{\sqrt{255^2 + 255^2 + 255^2}} = \frac{(1, 1, 1)}{\sqrt{3}}
$$

Ce vecteur est **normalisé** pour s’assurer que $$\( \vec{u} \)$$ ait une norme de 1.

---

### 2. Formule générale de la matrice de rotation

La matrice de rotation autour d’un axe défini par $$\( \vec{u} = (u_x, u_y, u_z) \)$$ pour un angle $$\( \theta \)$$ est :

$$
R = 
\begin{bmatrix}
\cos \theta + u_x^2(1 - \cos \theta) & u_x u_y (1 - \cos \theta) - u_z \sin \theta & u_x u_z (1 - \cos \theta) + u_y \sin \theta \\
u_y u_x (1 - \cos \theta) + u_z \sin \theta & \cos \theta + u_y^2(1 - \cos \theta) & u_y u_z (1 - \cos \theta) - u_x \sin \theta \\
u_z u_x (1 - \cos \theta) - u_y \sin \theta & u_z u_y (1 - \cos \theta) + u_x \sin \theta & \cos \theta + u_z^2(1 - \cos \theta)
\end{bmatrix}
$$

On utilise donc la formule de Rodrigues :

$$R = I + \sin(\theta) . K + (1 - \cos(\theta)) . K^2$$
---

### 3. Remplacement avec $$\( \mathbf{u} = \frac{(1, 1, 1)}{\sqrt{3}} \)$$

En remplaçant $$\( u_x = u_y = u_z = \frac{1}{\sqrt{3}} \)$$, la matrice devient :

$$
R =
\begin{bmatrix}
\cos \theta + \frac{1}{3}(1 - \cos \theta) & \frac{1}{3}(1 - \cos \theta) - \frac{\sin \theta}{\sqrt{3}} & \frac{1}{3}(1 - \cos \theta) + \frac{\sin \theta}{\sqrt{3}} \\
\frac{1}{3}(1 - \cos \theta) + \frac{\sin \theta}{\sqrt{3}} & \cos \theta + \frac{1}{3}(1 - \cos \theta) & \frac{1}{3}(1 - \cos \theta) - \frac{\sin \theta}{\sqrt{3}} \\
\frac{1}{3}(1 - \cos \theta) - \frac{\sin \theta}{\sqrt{3}} & \frac{1}{3}(1 - \cos \theta) + \frac{\sin \theta}{\sqrt{3}} & \cos \theta + \frac{1}{3}(1 - \cos \theta)
\end{bmatrix}
$$

---

# **Transformations in RGB Space**: Ensuring that colors remain within the RGB cube after transformations.

## 1. Analyse
Après la rotation $$C_0 \rightarrow C_1$$, la deuxième transformation doit ramener chaque point $$C_1$$ dans le cube RGB $$[0,255]^3$$ . Cette transformation s'appelle une **projection orthogonale** sur le cube.

## 2. Définition de la projection orthogonale :
1. Soit $$D_1 : (x,y,z) = \lambda(1,1,1)$$ l'axe de rotation.
2. Le point transformé $$C_1$$ est projette sur le cube des couleurs.
3. Si $$C_1$$ est hors du cube, on le projette sur plan orthogonal à $$D_1$$ , en passant par $$C_1$$ .
soit $$\vec{u} = (1,1,1)$$ le vecteur directeur de $$D_1$$ et $$C_1 = (x,y,z)$$ , alors :

**Projection orthogonale :** 

$$C_2 = C_1 - \begin{bmatrix} \frac{(C_1.\vec{u})}{||\vec{u}||^2} \end{bmatrix} \vec{u}$$

Avec $$||\vec{u}||^2 = 3$$ (norme au carre de $$\vec{u}$$) .

la formule utilise pour la transfomation est donc :

$$C_2 = C_1 - \begin{bmatrix} \frac{(C_1.\vec{u})}{3} \end{bmatrix} \vec{u}$$

---

# Thanks for your time

---