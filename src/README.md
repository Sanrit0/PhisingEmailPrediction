Detección de Emails de Phising usando Machine Learning

Datasets: *Al-Subaiey, A., Al-Thani, M., Alam, N. A., Antora, K. F., Khandakar, A., & Zaman, S. A. U. (2024, May 19). Novel Interpretable and Robust Web-based AI Platform for Phishing Email Detection. ArXiv.org. https://arxiv.org/abs/2405.11619*

El archivo phising_email.rar contiene un csv con todos los emails del resto de de archivos en uno.

Pasos seguidos en el proyecto:

- Limpieza de los datos: usando REGEX he quitado simbolos, URLs, y otros caracteres no necesarios.

- Usando el TfidfVectorizer creamos columnas con las palabras mas comunes, indicandole que descarte los stop words.

- Por último se ha probado con 3 modelos: Naive-Bayes, Regresión logistica y XGBoost.

El modelos que mejor resultado da es XGBoost, pero con un coste computacional alto. El de regresión logística da prácticamente el mismo resultado con un coste computacional mucho menor.

Los modelos estan guardados en la carpeta src/model en formato pickle.