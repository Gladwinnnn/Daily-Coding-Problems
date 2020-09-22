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