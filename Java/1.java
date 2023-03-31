import java.util.*;
public class GFG {
    public static void main(String args[])
    {
        int[][] arr = new int[3][3];

        System.out.println("enter the elements of matrix");

        int k = 1;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                arr[i][j] = k++;
            }
        }

        System.out.println("Matrix before Transpose ");
        //Меняем i на j и j на i
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(" " + arr[i][j]);
            }
            System.out.println();
        }

        System.out.println("Matrix After Transpose ");

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(" " + arr[j][i]);
            }
            System.out.println();
        }
    }
}