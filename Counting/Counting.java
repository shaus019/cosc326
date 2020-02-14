import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Counting {

	private long n;
	private long k;

	public Counting(long n, long k) {
		this.n = n;
		this.k = k;
	}

		/** 
	 * main method that read a input and generate a output by using scnanner
	 * can be read from file or user input
	 * */
	public static void main(String[] args) throws FileNotFoundException {

		Scanner sc = new Scanner(System.in);

		while (sc.hasNextLine()) {
			String line = sc.nextLine();
			
			try {
				String[] tokens = line.split("\\s+");
				
				long n = Long.parseLong(tokens[0]);
				long k = Long.parseLong(tokens[1]);

				if (n < k) {
					System.out.println(String.format("%d,%d: invalid input", n, k));
				} else {
					try {
						Counting cnk = new Counting(n, k);
						System.out.println(String.format("%d,%d: ", n, k) + cnk.getValue());
					} catch (Exception e) {
						System.out.println(String.format("%d,%d: overflow", n, k));
					}
				}
			} catch (Exception e) {
				System.out.println(line + ": " + "invalid input");
			}
		}
		sc.close();
	}

	/** generate an integer sequence from start to end */
	public ArrayList<Long> getNumbers(long start, long end) {
		// swap start and end if start > end
		if (start > end) {
			long temp = start;
			start = end;
			end = temp;
		}

		// get integer sequence
		ArrayList<Long> result = new ArrayList<>();
		for (long i = start; i <= end; i++) {
			result.add(i);
		}
		return result;
	}

	/** get the factors of number */
	public ArrayList<Long> getFactors(long number) {
		ArrayList<Long> result = new ArrayList<>();
		for (long i = 2; i < number / 2; i++) {
			while (number % i == 0) {
				result.add(i);
				number = number / i;
			}
		}
		return result;
	}

	/** calculation */
	public long getValue() {
		// get the numbers at up and down, then try to remove all the numbers in "down"
		ArrayList<Long> up = new ArrayList<>();
		ArrayList<Long> down = new ArrayList<>();

		if (k > n - k) {
			up = getNumbers(k + 1, n);
			down = getNumbers(1, n - k);
		} else {
			up = getNumbers(n - k + 1, n);
			down = getNumbers(1, k);
		}

		while (down.size() > 0) {
			ArrayList<Long> remain = new ArrayList<>();

			// for each number(toRemove) in down, try to find a number(v) in up where ( v %
			// toRemove == 0)
			for (int i = 0; i < down.size(); i++) {
				long toRemove = down.get(i);

				boolean found = false;
				for (int j = 0; j < up.size(); j++) {
					long v = up.get(j);

					if (v % toRemove == 0) {
						v = v / toRemove;
						up.set(j, v);
						found = true;
						break;
					}
				}

				// if not found, replace it with a list of it's factors
				if (!found) {
					remain.addAll(getFactors(toRemove));
				}
			}

			down = remain;
		}

		// product all numbers in up
		long result = 1;
		for (int i = 0; i < up.size(); i++) {
			result = Math.multiplyExact(result, up.get(i));
		}
		return result;
	}

}
