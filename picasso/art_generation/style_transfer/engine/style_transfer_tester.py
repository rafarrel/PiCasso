"""
    Build the graph for style transfer.

    From source [1]
"""
import picasso.art_generation.style_transfer.engine.transform as transform
import tensorflow as tf


class StyleTransferTester:

    def __init__(self, session, content_image, model_path):
        # Session
        self.sess = session

        # Input images
        self.x0 = content_image

        # Input model
        self.model_path = model_path

        # Image transform network
        self.transform = transform.Transform()

        # Build graph for art_styles transfer
        self._build_graph()

    def _build_graph(self):

        # Graph input
        self.x = tf.placeholder(tf.float32, shape=self.x0.shape, name='input')
        self.xi = tf.expand_dims(self.x, 0) # add one dim for batch

        # Result image from transform-net
        self.y_hat = self.transform.net(self.xi/255.0)
        self.y_hat = tf.squeeze(self.y_hat) # remove one dim for batch
        self.y_hat = tf.clip_by_value(self.y_hat, 0., 255.)

    def test(self):

        # Initialize parameters
        self.sess.run(tf.global_variables_initializer())

        # Load pre-trained model
        saver = tf.train.Saver()
        saver.restore(self.sess, self.model_path)

        # Get transformed image
        output = self.sess.run(self.y_hat, feed_dict={self.x: self.x0})

        return output





