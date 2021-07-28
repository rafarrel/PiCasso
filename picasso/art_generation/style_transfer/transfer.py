"""
    Run style transfer on selected content image using pre-trained
    style models.
"""
import picasso.art_generation.style_transfer.engine.utils as utils
import picasso.art_generation.style_transfer.engine.style_transfer_tester as style_transfer_tester
import tensorflow as tf
import time
from picasso.art_generation.style_transfer.engine.transfer_data import MAX_SIZE


def transfer(image, style_model_path):
    """
        Run the style transfer using a pre-trained style model.
    """

    # Load content image
    content_image = utils.load_image(image, max_size=MAX_SIZE)

    # Open session
    soft_config = tf.ConfigProto(allow_soft_placement=True)
    soft_config.gpu_options.allow_growth = True # to deal with large image
    sess = tf.Session(config=soft_config)

    # Build the graph
    transformer = style_transfer_tester.StyleTransferTester(session=sess,
                                                            model_path=style_model_path,
                                                            content_image=content_image,
                                                            )
    # Execute the graph
    start_time = time.time()
    output_image = transformer.test()
    end_time = time.time()

    # Report execution time
    shape = content_image.shape  # (batch, width, height, channel)
    print('Execution time for a %d x %d image : %f msec' % (
        shape[0], shape[1], 1000. * float(end_time - start_time) / 60))

    # Save result
    return utils.save_image(output_image)



