import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.ArrayList;
import java.util.List;

@SpringBootApplication
public class PrimeCheckerApplication {
    public static void main(String[] args) {
        SpringApplication.run(PrimeCheckerApplication.class, args);
    }
}

@Controller
class PrimeController {

    @GetMapping("/")
    public String home() {
        return "index";
    }

    @PostMapping("/check-prime")
    public String checkPrime(@RequestParam("number") String number, Model model) {
        try {
            int n = Integer.parseInt(number);
            boolean isPrime = isPrime(n);
            model.addAttribute("result", isPrime ? n + " is a prime number." : n + " is not a prime number.");
        } catch (NumberFormatException e) {
            model.addAttribute("result", "Invalid input. Please enter a valid integer.");
        }
        return "index";
    }

    @PostMapping("/extract-primes")
    public String extractPrimes(@RequestParam("text") String text, Model model) {
        List<Integer> primes = extractPrimesFromString(text);
        model.addAttribute("result", "Prime numbers: " + (primes.isEmpty() ? "None" : primes));
        return "index";
    }

    private boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    private List<Integer> extractPrimesFromString(String text) {
        List<Integer> primes = new ArrayList<>();
        String[] tokens = text.split("\\D+"); // Split by non-digit characters
        for (String token : tokens) {
            if (!token.isEmpty()) {
                try {
                    int number = Integer.parseInt(token);
                    if (isPrime(number)) {
                        primes.add(number);
                    }
                } catch (NumberFormatException ignored) {
                    // Ignore invalid numbers
                }
            }
        }
        return primes;
    }
}
