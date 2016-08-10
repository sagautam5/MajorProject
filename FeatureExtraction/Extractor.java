package FeatureExtraction.org.classes;
/** 
 * Image Feature Extraction in User Mode
 *
 * @author Sagar Gautam
 * @version 1.0
 * @since 2016-07-25
 */
public class Extractor{

    int factor;                                         /** Times by which image has to be reduced in all dimension */
    String image_Location;                              /** Location of the image file of User input                */
    String text_Location = "Resource/User/Text.txt";    /** Location of text file with User input image features    */

    double[][][] Image = new double[144][208][176];     /** Array of User input image voxels value(gray scale value)*/
    double[][][] Data_Nn = new double[9][13][11];       /** Reduced Image array after interpolation                 */


    Extractor(String image_Location,int factor){

        this.image_Location = image_Location;
        this.factor = factor;
    }

    /** 
     * This is the method to calculate image features
     * Stores features in text file 
     * Returns feature vector
     */
    double[] Write(){

        double[] volumes = new double[3];       /** Feature Vector */

        /** Reading image from file */
        ImageReader imageReader = new ImageReader(image_Location);
        
        /** Writing 175 images */
        imageReader.writeImagefiles();

        /** Image array of full size */
        Image = imageReader.getImage();


        /** Image compression by interpolation */
        Compress compress = new Compress(Image);

        /** Reduced image */
        Data_Nn = compress.getReduced();

        /** Writing Features in a text file */
        ImageWriter imageWriter = new ImageWriter(Data_Nn,text_Location);
        
        /** get feature  vector from compressed image */
        volumes = imageWriter.getVolume();
        return volumes;
    }
}
