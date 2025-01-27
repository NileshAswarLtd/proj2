import java.util.regex.*;
import java.util.ArrayList;
import java.util.List;

public class PrimeChecker {

    // Function to check if a number is prime
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        else if (n == 2) return true;
        else if (n % 2 == 0) return false;

        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }

    // Function to find all primes in a string
    public static List<Integer> findPrimesInString(String input) {
        Pattern pattern = Pattern.compile("\\d+");
        Matcher matcher = pattern.matcher(input);

        List<Integer> primes = new ArrayList<>();
        while (matcher.find()) {
            int num = Integer.parseInt(matcher.group());
            if (isPrime(num)) {
                primes.add(num);
            }
        }
        return primes;
    }

    public static void main(String[] args) {
        System.out.println("Enter a string:");
        Scanner scanner = new Scanner(System.in);
        String inputString = scanner.nextLine();

        List<Integer> primeNumbers = findPrimesInString(inputString);

        System.out.println("Prime numbers found in the string: " + primeNumbers);
    }
}