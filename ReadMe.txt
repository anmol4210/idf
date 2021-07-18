flask_app: To run the flask app and test the model run 'python app.py' in the flask_app folder. The post request (localhost:5000/classify) expects 'text' inside the body. I have also attached a screen shot for better understanding.

training: All the preprocessing and training code is available under the folder training.

Before training the model my first step was to understand the data, clean the data and extract all the relevant information present.
Once I extracted the data I stored it in separate groups depending upon the class it belongs data. (data/train/)
Since the volume of data was small, I thought it will be good to use machine learning algorithm rather than deep learning algorithm.
To train the model my first step was to vectorize the data followed by creating a training pipeline and fitting the model.

Future Scope:
As the volume of data increases we can try various transforer based architectures like Bert, Albert, RObert, XLNet, etc.
