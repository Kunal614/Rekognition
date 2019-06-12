from Rekognition.settings import BASE_DIR
from corelib.facenet.utils import load_model
from corelib.facenet.align import detect_face
import tensorflow as tf
import os


upload_path = os.path.join(BASE_DIR, 'cceface/uploads')
embeddings_path = os.path.join(BASE_DIR, 'corelib/embeddings')
allowed_set = set(['png', 'jpg', 'jpeg', 'PNG', 'JPEG', 'JPG'])
model_path = BASE_DIR + '/corelib/facenet/model/2017/20170512-110547.pb'
facenet_model = load_model(model_path)
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
image_size = 160
images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
facenet_persistent_session = tf.Session(graph=facenet_model, config=config)
pnet, rnet, onet = detect_face.create_mtcnn(sess=facenet_persistent_session, model_path=None)