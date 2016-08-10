package FeatureExtraction.org.classes;

/** 
 * This is the class to compress full size image step wise
 * according to the compressing factor
 *
 * @author Sagar Gautam
 * @version 1.0
 * @since 2016-05-17
 */
public class Compress{
    
    /** These are the four arrays as we have to compress in four stage 2^4 = 16(factor)*/
    double[][][] A1 = new double[72][104][88];
    double[][][] A2 = new double[36][52][44];
    double[][][] A3 = new double[18][26][22];
    double[][][] A4 = new double[9][13][11];
    
    Reduce R1,R2,R3,R4; /** four version of reduced array */

    Compress(double[][][] Image){
    
        /** Step 1 */
        R1 = new Reduce(Image);
        A1 = R1.Nearest(2);
        // A1 = R1.Bilinear(2);
        
        /** Step 2 */     
        R2 = new Reduce(A1);
        A2 = R2.Nearest(2);
        //A2 = R2.Bilinear(2);
        
        /** Step 3 */
        R3 = new Reduce(A2);
        A3 = R3.Nearest(2);
        //A3 = R3.Bilinear(2);
        
        /** Step 4 */
        R4 = new Reduce(A3);
        A4 = R4.Nearest(2);
        //A4 = R4.Bilinear(2);

    }
    
    /** This is the method to return the 16 times reduced array */
    double[][][] getReduced(){
        
        return A4;
    }

    /** Display 16 times reduced array. */
    void show(double[][][] arr,String name){
    
        System.out.println(name+"Array");
        Vector Size = new Vector(arr.length,arr[0].length,arr[0][0].length);
        
        for(int i=0;i<Size.x;i++){
          
            for(int j=0;j<Size.y;j++){
            
                for(int k=0;k<Size.z;k++){
                
                    System.out.print(arr[i][j][k]+" ");
                }
                System.out.println();
            }
            System.out.println();
        }

}
}

