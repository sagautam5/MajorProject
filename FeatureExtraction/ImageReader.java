package FeatureExtraction.org.classes;

import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;

import java.io.*;
import java.util.*;
import java.awt.*;

import java.nio.*;
import java.nio.file.*;

/**
 * <h1> Read Image From File !</h1>
 * 
 * training and testing .img files are loaded
 * binery representation of images is changed to gray scale representation 
 * grayscale value of each voxel is kept on 3d array
 *
 * @author Sagar Gautam
 * @since 2016-3-10
 */
public class ImageReader{

    double[][][] Image = new double[176][208][176];
    short[][][] RawImage = new short[176][208][176];
    double[][][] smallImage = new double[144][208][176];
    public static final int TYPE_INT_RGB = 1;
    
    /**
     * This is the constructor of Image Reader
     * Method read from .img file and takes whole bytes and performs 
     * operations to get gray scale values
     */
    ImageReader(String filename){

        try{
        
            Path path = Paths.get(filename);

            byte[] byteArray = Files.readAllBytes(path);
            ByteBuffer bbuffer = ByteBuffer.wrap(byteArray);
            
            /** Set the Byte Order */
            bbuffer.order(java.nio.ByteOrder.BIG_ENDIAN);
            
            double data = 0.0d;
            
            for(int i=0; i<176; i++){
            
                for(int j=0; j<208;j++){
                
                    for(int k=0; k<176; k++){

                    /** FIXME: check using bbuffer.hasRemaining */
                        short gray_value = bbuffer.getShort();
                    
                    /** converting 16bit grayscale to 8bit byte shifting */
                    /** x = (short)(x%256) */
                    
                    gray_value = (short)(gray_value/16);
                    
                    RawImage[i][j][k] = gray_value;
                    
                    /** Image segmentation process 
                     * to get four different parts of the MRI scan which are :
                     * Background, dark gray matter, light gray matter and white matter
                     */

                    if(gray_value>=0 && gray_value<5)           gray_value = 0;

                    else if(gray_value>=5 && gray_value<38)     gray_value = 85;
                    
                    else if(gray_value>=38 && gray_value<72)    gray_value = 170;
                    
                    else if(gray_value>=72 && gray_value<256)   gray_value = 255;

                    data = (double)(gray_value);
        		    Image[i][j][k] = data;
                    }
                }
            }

            /** Unwanted Image Layer Removal */
            for(int a=0;a<144;a++){
                
                for(int b=0;b<208;b++){
                
                    for(int c=0;c<176;c++){
                    
                        smallImage[a][b][c] = Image[a+8][b][c];
                    }
            
                }
            }

        }catch(Exception e){

            System.out.println(e);
        }
    }
    
    /** This is the method to return an image after the removal of the unwanted layers. */
    double[][][] getImage(){
	
        return smallImage;
	}

    /** Method to write 176 distinct MRI scan layers */
    void writeImagefiles(){
        
        try{
            short gray = 0;
            
            for(int i=0;i<176;i++){
            
                BufferedImage Layer = new BufferedImage(208,176,TYPE_INT_RGB);
                
                for(int j=0;j<208;j++){
                
                    for(int k=0;k<176;k++){
                    
                        gray = (short)(RawImage[i][j][k]+(short)0); /**to increase contrast change value 0 */
                        if(gray>255) gray = 255;
                        Color color = new Color(gray,gray,gray);
                        Layer.setRGB(j,k,color.getRGB());
                    
                    }
                }
                File op = new File("Resource/Layers/layer"+(i+1)+".jpg");
                ImageIO.write(Layer,"jpg",op);
            
            }
        
        }catch(Exception e){
        
            System.out.println("Error:"+e.getMessage());
        }

    }
}

