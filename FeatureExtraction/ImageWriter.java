package FeatureExtraction.org.classes;

import java.io.*;
import java.util.*;
/**
 * This is the class to calculate image features as the feature vector
 * Finally features are stored in text files.
 *
 * @author Sagar Gautam
 * @version 1.0
 * @since 2016-04-30
 */
public class ImageWriter{
    
    Vector Size;                        /** Size of Image */
    String filename = new String();     /** file name of .img file */
    
    double matterW = 0.0d;              /** white matter */
    double matterG = 0.0d;              /** dark gray matter */
    double matterg = 0.0d;              /** light gray matter */
               

    ImageWriter(double[][][] Data, String filename){
		
        int no1_count =0;
        this.filename = filename;
       
        Size = new Vector(Data.length,Data[0].length,Data[0][0].length);
        
        /** Calculation of volume of matters */
        try{
            
            BufferedWriter output = null;
            File file = new File(filename);
            output = new BufferedWriter(new FileWriter(file));
            
            double data = 0;
            String BitPat = "",WBP="",GBP="",gBP="";

            for(int i=0;i<Size.x;i++){ 
    
                for(int j=0;j<Size.y;j++){
                
                    for(int k=0;k<Size.z;k++){
    
                   data = (double)(Data[i][j][k]);

                   if(data == 85.0d) matterG++;
                   if(data == 170.0d) matterg++;
                   if(data == 255.0d) matterW++;
                    
                    }
                }     
            }

            /** Feature Normalization into (0,1) range */
            matterG = matterG/398.0d;
            matterg = matterg/398.0d;
            matterW = matterW/398.0d;

            BitPat = matterG+" "+matterg+" "+matterW; 
            output.write(BitPat);
            output.close();

        }catch(Exception e){

            System.out.println("ERROR:"+e.getMessage());
        }

        System.out.println(filename+":File Sucessfully Written");
    }
    
    /** Method to return feature vector */
    double[] getVolume(){
        
        double[] Feature = new double[3];
        
        Feature[0] = matterG;
        Feature[1] = matterg;
        Feature[2] = matterW;
        
        return Feature;
    } 
}
