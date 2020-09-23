// Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
// For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

import java.util.*;

public class Q2{
    static ArrayList<Integer> checkMethod(int[] intArray){
        ArrayList<Integer> resultArray= new ArrayList<Integer>();
        for (int i = 0; i < intArray.length; i++){
            int result = 1;
            int placeHolder = intArray[i];
            for (int j = 0; j < intArray.length; j++){
                if (intArray[j] != placeHolder){
                    result *= intArray[j];
                }
            }
            resultArray.add(result);
        }
        return resultArray;
    }
    public static void main(String[] args){
        int[] intArray = {1, 2, 3, 4, 5};
        System.out.print(checkMethod(intArray));
    }
}