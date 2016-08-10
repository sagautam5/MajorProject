package FeatureExtraction.org.classes;

import java.util.*;
/**
 *
 * Class for integration of basic  image preprocessing stages that
 * loads 3d images, performs preprocessing and finally gives a one
 * dimensional feature vector.
 * 
 *
 *
 * @author Sagar Gautam
 * @version 1.0
 * @since 2016-03-11
 */
public class Dementia{

    /** This factor gives amount of times in each dimension of the 3d image 
     * has to be reduced to get compressed image.
     */

    public static int factor = 16;
    
    /**
     * No of training data set.
     */ 
    public static int file_d_train = 75;    /** demented     */
    public static int file_nd_train = 107;  /** not demented */

    /**
     * Location of the training data set.
     */
    public static String Demented_Path_train = "Resource/TrainData/Demented/";
    public static String NotDemented_Path_train = "Resource/TrainData/NotDemented/";
    
    /**
     * File name of the training image files.
     */
    public static String[] Demented_train = new String[file_d_train];
    public static String[] NotDemented_train = new String[file_nd_train];
    
    /**
     * Name of files containing feature vector for training data set.
     */
    public static String[] Text_Demented_train = new String[file_d_train];
    public static String[] Text_NotDemented_train = new String[file_nd_train];
    
    /**
     * No of testing data set.
     */
    public static int file_d_test = 25;
    public static int file_nd_test = 28;

    /**
     * Location of the testing data set.
     */
    public static String Demented_Path_test = "Resource/TestData/Demented/";
    public static String NotDemented_Path_test = "Resource/TestData/NotDemented/";
   
    /**
     * File name of the testing image files.
     */
    public static String[] Demented_test = new String[file_d_test];
    public static String[] NotDemented_test = new String[file_nd_test];

    /**
     * Name of the files containing feature vector of testing data set. 
     */
    public static String[] Text_Demented_test = new String[file_d_test];
    public static String[] Text_NotDemented_test = new String[file_nd_test];
    
    /**
     * Array containing 3d voxels of a MRI scan
     * 3d MRI scan has dimension 176 * 208 * 176 with 6443008 voxels 
     * Which are stored in 3 dimensional array 
     * Image after removing unwanted 32 layers with black voxels only 
     * so, final size of Image is 144 * 208 * 176.
     */
    public static double[][][] Image = new double[144][208][176];

    /**
     * Array Containing voxels of MRI scan after Nearest Neighbour interpolation
     * Size of the image after compression 1287 voxels
     * 9 * 13 * 11
     */
    public static double[][][] Data_Nn  = new double[9][13][11];
    
    /** Method for generation of MRI Scan location and file name   */
    public static String[] FileNames(String path, int count){
    
        String[] Files = new String[count];
       
        for(int i=0;i<count;i++){
        
            Files[i] = path+"Image/Image"+i+".img";
        }
        
        return Files;
    }

    /** Method for generation of the file name containing feature vector.  */
    public static String[] Text_FileNames(String path, int count){
    
        String[] Files = new String[count];
       
        for(int i=0;i<count;i++){
        
            Files[i] = path+"Nearest/Image"+i+".txt";
        }
        
        return Files;
    }
    
    /** Preprocessing of MRI scan to extract feature vector.    */
    public static void Write(String[] ImageFile, String[] TextFile, int count){

        for(int i = 0; i < count; i++){
        
            /** Read Image File */
            ImageReader imageReader = new ImageReader(ImageFile[i]);
            Image = imageReader.getImage();

            /** Compress Image Data from 144*208*176 to 9*13*11 */
            Compress COM = new Compress(Image);
            Data_Nn = COM.getReduced();

            /** Write Compressed Data into Text file */
            ImageWriter imageWriter = new ImageWriter(Data_Nn,TextFile[i]);
        }
        
    }

    public static void System(String Action){

        String operation = Action;          /** Train  */

        /**Training and Testing mode */
        if(operation.equals("Train")){
            
            /** Training data file name extraction. */
            Demented_train = FileNames(Demented_Path_train, file_d_train);
            NotDemented_train = FileNames(NotDemented_Path_train, file_nd_train);
            
            /** Training data feature vector file name extraction. */
            Text_Demented_train = Text_FileNames(Demented_Path_train, file_d_train);
            Text_NotDemented_train = Text_FileNames(NotDemented_Path_train, file_nd_train);
            
            /** Training feature vector extraction and storing in file. */
            Write(Demented_train, Text_Demented_train, file_d_train);
            Write(NotDemented_train,Text_NotDemented_train, file_nd_train);
        
            /** Testing data file name extraction. */
            Demented_test = FileNames(Demented_Path_test, file_d_test);
            NotDemented_test = FileNames(NotDemented_Path_test, file_nd_test);
        
            /** Training data feature vector file name extraction. */
            Text_Demented_test = Text_FileNames(Demented_Path_test, file_d_test);
            Text_NotDemented_test = Text_FileNames(NotDemented_Path_test, file_nd_test);
            
            /** Training feature vector extraction and storing in file. */
            Write(Demented_test, Text_Demented_test, file_d_test);
            Write(NotDemented_test,Text_NotDemented_test, file_nd_test);
        }
    }

    public static String System(String Action, String Location){
        
        /** User Mode */
        
        String operation = Action;          /** Test */
        double[] volumes = new double[3];   /** volume of dark Gray, light Gray and White matter */
        if(operation.equals("Test")){

            Extractor extractor = new Extractor(Location,factor); /** Run time feature vector extrator in User Mode. */
            volumes = extractor.Write();                          /** Storage of feature vector in a text file. */
            System.out.println("Test Image Feature Extracting.....");
        }
    
    /**Feature Vector */
    String feature = volumes[0]+" "+volumes[1]+" "+volumes[2];	

    return feature;
    }

    /**main function */
    public static void main(String[] args){

    }
}
