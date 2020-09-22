// Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
// Bonus: Can you do this in one pass?

public class Q1{
    static boolean checkMethod(int[] intArray, int k){
        for (int i = 0; i < intArray.length; i++){
            int temp = intArray[i];
            for (int j = i + 1; j < intArray.length; j++){
                if (temp + intArray[j] == k){
                    return true;
                }
            }
        } return false;
    }
    public static void main(String[] args){
        int[] intArray = {10, 15, 3, 7};
        int k = 17;
        System.out.print(checkMethod(intArray, k));
    }
}