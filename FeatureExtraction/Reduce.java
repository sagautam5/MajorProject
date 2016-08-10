package FeatureExtraction.org.classes;

import java.io.*;

import java.util.*;

/**
 * Class used in order to reduce full size MRI scan image by 16 times in each dimension
 * Total reduction volumetrically by 16*16*16 = 4096 times.
 *
 * @author Sagar Gautam
 * @since 2016-02-25
 */
public class Reduce{

    Vector size,size_Nn,size_Bl;            /** Size of Original, Nearest Neighbour and bilineear interpolated Image    */
    double[][][] Voxel;                     /** Original array of full size MRI scan.                                   */
    double[][][] Voxel_Nn;                  /** Image array after Nearest Neihbour interpolation.                       */
    double[][][] Voxel_Bl;                  /** Image array  after Bilinear interpolation.                              */

    Reduce(double[][][] Data){
        
        size  = new Vector(Data.length,Data[0].length,Data[0][0].length); 
        Voxel = new double[size.x][size.y][size.z];
        Voxel = Data;
    }

    /**
     * This method takes amount by which each dimension of a 3d image array
     * has to be compressed and then reduces the image using Nearest
     * Neighbour Interpolation and finally it returns compressed 3d image.
     */
    double[][][] Nearest(int factor){

        size_Nn = new Vector(size.x/factor,size.y/factor,size.z/factor);
        Voxel_Nn = new double[size_Nn.x][size_Nn.y][size_Nn.z];

        for(int i=0;i<size_Nn.x;i++){
            
            for(int j=0;j<size_Nn.y;j++){
              
                for(int k=0;k<size_Nn.z;k++)
                    
                    Voxel_Nn[i][j][k] = Voxel[factor*i][factor*j][factor*k]; 
            }
        }
        
        return Voxel_Nn;
    }


    /**
     * This method takes amount by which each dimension of a 3d image array
     * has to be compressed and then reduces the image using Bilinear 
     * Interpolation and finally it returns Compressed 3d image.
     */
    double[][][] Bilinear(int factor){
    
        size_Bl = new Vector(size.x/factor,size.y/factor,size.z/factor);
        Voxel_Bl = new double[size_Bl.x][size_Bl.y][size_Bl.z];

        double sum = 0.0d;
        for(int i=0;i<size_Bl.x;i++){
          
            for(int j=0;j<size_Bl.y;j++){
            
                for(int k=0;k<size_Bl.z;k++){

                    double mean = 0.0d;
                
                    for(int p=i*factor;p<factor*i+factor;p++){
                    
                        for(int q=j*factor;q<j*factor+factor;q++){
                        
                            for(int r=k*factor;r<k*factor+factor;r++){
                                
                                mean+= Voxel[p][q][r];

                                sum += Voxel[p][q][r];
                            }
                        }
                    }
                        
                    mean = mean/(factor*factor*factor);
		            mean = (int)(mean);
                    
                    Voxel_Bl[i][j][k] =mean;
                }
            }
        }
                    
        return Voxel_Bl;
    }


}
