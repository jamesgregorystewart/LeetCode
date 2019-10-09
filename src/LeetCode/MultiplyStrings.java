package LeetCode;

public class MultiplyStrings {
    public static void main(String[] args) {
        MultiplyStrings solution = new MultiplyStrings();
        System.out.println(solution.multiply("123", "456"));
    }

    public String multiply(String num1, String num2) {
        CharSequence seq1 = num1;
        CharSequence seq2 = num2;
        StringBuilder resultBuilder = new StringBuilder();
        int p1 = seq1.length();
        int p2 = seq2.length();
        int[] products = new int[Math.min(p1, p2)];
        int resultLength = p1+p2-1;
        int multP = 0;
        int factor = 1;
        int carryover = 0;

        //build array of products
        for (int i = p1-1; i >= 0; i--) {
            carryover = factor = 0;
            int runningSum = 0;
            for (int j = p2-1; j >= 0; j--) {
                runningSum += (((Integer.valueOf(seq1.charAt(i)) * Integer.valueOf(seq2.charAt(j))) + carryover)%10)*factor;
                carryover = (((Integer.valueOf(seq1.charAt(i)) * Integer.valueOf(seq2.charAt(j))) + carryover)/10)*factor;
                factor++;
            }
            products[multP++] = runningSum;
        }

        carryover = 0;
        int productLength = Integer.toString(products[0]).length();

        //Build the result string
        for (int i = 0; i < resultLength; i++) {
            int sum = 0;
            if (i < productLength) {
                for (int j = 0; j <= i; j++) {
                    sum += products[j] % ((j+1) * 10);
                }
            } else {
                //start from i - (productLength - 1) and go to products.length-1;
                for (int j = i - (productLength - 1); j < products.length; j++) {
                    sum += products[j] % ((j+1) * 10);
                }
            }
            int remainder = sum  + carryover % 10;
            carryover = sum + carryover / 10;
            resultBuilder.append(Integer.toString(remainder));
        }
        if (carryover != 0) resultBuilder.append(Integer.toString(carryover));
        return resultBuilder.reverse().toString();
    }
}

