public class SumCalculator {

    public int calculateSum(int[] numbers) {
        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            sum += numbers[i];
        }
        return sum;
    }

    public static void main(String[] args) {
        SumCalculator calculator = new SumCalculator();
        int[] numbers = {1, 2, 3, 4, 5};
        int result = calculator.calculateSum(numbers);
        System.out.println("Sum: " + result);
    }
}
