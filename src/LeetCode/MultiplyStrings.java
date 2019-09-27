//package LeetCode;
//
////p1 = shorter
////p2 = longer
//
//public class MultiplyStrings {
//    public String multiply(String num1, String num2) {
//        CharSequence seq1 = num1.length() <= num2.length() ? num1 : num2; //seq1 is the shorter
//        CharSequence seq2 = num1.length() <= num2.length() ? num2 : num1; //seq2 is the longer
//        StringBuilder resultBuilder = new StringBuilder();
//        int p1 = seq1.length();
//        int p2 = seq2.length();
//        int[] products = new int[p1];
//        int multP = 0;
//        int factor;
//        int carryover;
//
//        //build array of products
//        for (int i = p1-1; i >= 0; i--) {
//            carryover = 0;
//            factor = 1;
//            int runningSum = 0;
//            for (int j = p2-1; j >= 0; j--) {
//                runningSum += (((Character.getNumericValue(seq1.charAt(i)) * Character.getNumericValue(seq2.charAt(j))) + carryover)%10)*factor;
//                carryover = (((Character.getNumericValue(seq1.charAt(i)) * Character.getNumericValue(seq2.charAt(j))) + carryover)/10)*factor;
//                factor++;
//            }
//            products[multP++] = runningSum;
//        }
//
//        carryover = 0;
//        int productLength = Integer.toString(products[0]).length();
//        int loopOneLength = productLength + products.length - 1;
//
//        //Build the result string
//        for (int i = 0; i < loopOneLength; i++) {
//            int sum = 0;
//            if (i < productLength) {
//                for (int j = 0; j < pro; j++) {
//                    sum += products[j] % ((j+1) * 10);
//                }
//            } else {
//                //start from i - (productLength - 1) and go to products.length-1;
//                for (int j = i - (productLength - 1); j < products.length; j++) {
//                    sum += products[j] % ((j+1) * 10);
//                }
//            }
//            int remainder = (sum  + carryover) % 10;
//            carryover = (sum + carryover) / 10;
//            resultBuilder.append(Integer.toString(remainder));
//        }
//        if (carryover != 0) resultBuilder.append(Integer.toString(carryover));
//        return resultBuilder.reverse().toString();
//    }
//}
