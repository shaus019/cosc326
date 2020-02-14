import java.util.*;
import java.io.*;

/**
 * This program using recursive algorithm that reads two lines of a file, one
 * defines the lights with letters, eg. A B C D, another line defines a set of
 * edges. eg. AB generate the list of button that either turn off (or turn on)
 * all the light, which is the optimal solution.
 * 
 * @author: Orlando Yuan, Usman Shah
 */
public class LightControl {
	static int num = 10;
	/** <name of light, state of light (1 on, 0 off)> */
	static Map<String, Integer> lightMap;
	/**
	 * one switch in each line, list the lights that controlled by certain switch
	 */
	static LinkedHashMap<Character, ArrayList<Character>> control;
	/** sum of the value of solveLightMap */
	static int min = Integer.MAX_VALUE;
	/** number of lights that on */
	static int ON = 0;
	/** switch order, 0 = not press, 1 = press */
	static int[] swichOrder;
	/** two boolean variables that used to break the loop */
	static boolean isBreak = false;
	static boolean hasSolve = false;
	/** store like eg. A, 1 first param = light(str) second param = 0 or 1 */
	static Map<String, Integer> solveLightMap;
	/** store input */
	static String[] line1Arr;
	static String[] lightArray;
	/** a copy of control using as a local variable */
	static ArrayList<ArrayList<Character>> tempControl;

	/**
	 * main method set a scanner read input from file using the return value of
	 * getInputList() calls optimal() to do further execution
	 */
	public static void main(String[] args) {

		boolean correct = true;
		// set the scanner to read from a file
		Scanner sc = new Scanner(System.in);
		String path = "";
		System.out.println("please input file path: ");

		// if the path is correct, execute
		while (correct) {
			path = sc.nextLine();
			File file = new File(path);
			// if the file doesnt exist, print the error message
			if (!file.exists()) {
				System.out.println("file path error, please input again: ");
			} else {
				System.out.println("file path correct. ");
				System.out.println();
				correct = false;
			}
		}

		// added input file into list
		ArrayList<String> arrayList = getInputList(path);

		// determine how many input we have
		int totalQuestionNum = arrayList.size();
		boolean invalid = true;

		// display each input with a number to avoid confusion
		for (int i = 0; i < totalQuestionNum; i = i + 2) {
			String output = "Q" + (i / 2 + 1) + ": ";
			System.out.print(output);
			// relation
			lightArray = arrayList.get(i).split(" ");
			for (int lightindex = 0; lightindex < lightArray.length; lightindex++) {
				// length of each char in the first line must be equal to 1
				if (lightArray[lightindex].length() != 1) {
					System.out.println("invalid value");
					System.out.println();
					invalid = false;
					break;
				}
			}
			if (invalid) {
				if (i == totalQuestionNum - 1) {
					optimal(arrayList.get(i), arrayList.get(i));
				} else {
					optimal(arrayList.get(i), arrayList.get(i + 1));
				}

			} else {
				invalid = true;
			}
		}
	}

	/**
	 * method that store the input into an arraylist and return
	 */
	public static ArrayList<String> getInputList(String inputPath) {

		ArrayList<String> arrayList = new ArrayList<>();

		try {
			FileReader fr = new FileReader(inputPath);
			BufferedReader bf = new BufferedReader(fr);
			String str;

			while ((str = bf.readLine()) != null) {
				arrayList.add(str);
			}

			bf.close();
			fr.close();

		} catch (IOException e) {
			e.printStackTrace();
		}

		return arrayList;

	}

	/**
	 * method that split the input and prepare for further calculation by calling
	 * solve()
	 */
	public static void optimal(String lightArray, String lightRelation) {

		// split the input
		line1Arr = lightArray.split(" ");
		lightMap = new LinkedHashMap<>();
		control = new LinkedHashMap<>();
		// add to list
		for (int i = 0; i < line1Arr.length; i++) {
			lightMap.put(line1Arr[i], 1);
			ArrayList<Character> characters = new ArrayList<>();
			characters.add(line1Arr[i].charAt(0));
			control.put(line1Arr[i].charAt(0), characters);
		}
		// split the input
		String[] line2Arr = lightRelation.split(" ");

		// convert to char
		for (int i = 0; i < line2Arr.length; i++) {
			char[] chars = line2Arr[i].toCharArray();
			// add to list
			for (int j = 1; j < chars.length; j++) {
				control.get(line2Arr[i].charAt(0)).add(chars[j]);
			}
		}

		// System.out.println("relations: ");
		// for (Map.Entry<Character, ArrayList<Character>> entry : control.entrySet()) {
		// System.out.println(entry.getValue());
		// }

		solve();

	}

	/**
	 * method that does the final calculation it will be called in optimal()
	 */
	public static void solve() {

		// in the first part copy the value of control to tempControl
		Set<Map.Entry<Character, ArrayList<Character>>> entrySet = control.entrySet();
		tempControl = new ArrayList<>();
		for (Map.Entry<Character, ArrayList<Character>> entry : entrySet) {
			tempControl.add(entry.getValue());
		}

		// local variables
		isBreak = false;
		hasSolve = false;
		ON = 0;
		min = Integer.MAX_VALUE;

		// initialize the value of solveLightMap that all to 1
		// as the initial state supposes that all lights are on at the start
		solveLightMap = new LinkedHashMap<>();
		for (Map.Entry<String, Integer> entry : lightMap.entrySet()) {
			solveLightMap.put(entry.getKey(), entry.getValue());
		}
		swichOrder = new int[tempControl.size()];

		// System.out.println("optimal solution: ");

		// call the recursion method
		backTrace(0);
		// if the status didn't reach 0
		if (min != 0) {
			// number of the lights are still on
			ON = min;
			swichOrder = new int[tempControl.size()];
			// tranverse lightMap and copy the value of it into solveLightMap
			for (Map.Entry<String, Integer> entry : lightMap.entrySet()) {
				solveLightMap.put(entry.getKey(), entry.getValue());
			}
			// recursion
			backTrace(0);
		}

	}

	/**
	 * method that performs the recursive algorithm the return value will be used in
	 * solve()
	 */
	public static void backTrace(int cur) {

		// if the last switch is arrived
		if (isBreak)
			return;

		// cur starts at 0, in a case A B C D, AC AD BD CA when cur reaches 4 excute
		// this loop
		if (cur == tempControl.size()) {
			int sum = 0;
			// sum up the number of the lights that are on
			for (Map.Entry<String, Integer> entry : solveLightMap.entrySet()) {
				sum += entry.getValue();
			}

			// min = the minimum number of the current lights that are on
			min = sum < min ? sum : min;
			// if sum = 0 means there is an optimal solution
			if (sum == ON) {
				isBreak = true;
				if (ON == 0) {
					hasSolve = true;
				}

				for (int i = 0; i < swichOrder.length; i++) {
					// store the pressed switches
					if (swichOrder[i] == 1) {
						System.out.print(lightArray[i]);
					}
				}
				System.out.println();
				System.out.println();
			}

			return;
		}

		// suppose the switch is not pressed (0)
		swichOrder[cur] = 0;
		// call backTrace(1), recursing, and so on until the condition reached
		backTrace(cur + 1);
		// change the value of solveLightMap, in this case tempControl.get(cur).size() =
		// 4
		for (int i = 0; i < tempControl.get(cur).size(); i++) {
			// if is on
			if (solveLightMap.get(String.valueOf(tempControl.get(cur).get(i))) == 1) {
				// shut to off
				solveLightMap.put(String.valueOf(tempControl.get(cur).get(i)), 0);
			} else {
				solveLightMap.put(String.valueOf(tempControl.get(cur).get(i)), 1);
			}
		}

		// suppose the switch is pressed (1)
		swichOrder[cur] = 1;
		// call backTrace(1), recursing, and so on until the condition reached
		backTrace(cur + 1);
		// change the value of solveLightMap
		for (int i = 0; i < tempControl.get(cur).size(); i++) {
			if (solveLightMap.get(String.valueOf(tempControl.get(cur).get(i))) == 1) {
				solveLightMap.put(String.valueOf(tempControl.get(cur).get(i)), 0);
			} else {
				solveLightMap.put(String.valueOf(tempControl.get(cur).get(i)), 1);
			}
		}
	}

}
