/*importing all the librariers which i am working with*/ 
import java.util.Scanner;
import java.lang.Character;//for wrapping the value of char into an object
import java.lang.StringBuilder;// for mutable sequence of characters
import java.util.Arrays;//to download array
public class Puzzle{

    public static String operandBuilder = "";
    public static void main(String[]args){
        String inputNumbers;//the input numbers
        String[] stringSplitter = null;
        int[] numbers = null;//for putting the numbers into an array
        char operation;//that will be the operation which we need to perfor L or R
        String targetOp;//the target which we need to get
        int i;//to go through the input numbers
        long target;//for the target value
        int length = 0;//that will be the length of the array
        int found = 0;//if the target is found or not
        int minimumResult;
        int maximumResult;
        Scanner scanner = new Scanner(System.in);//reading the input from the input file
        while(scanner.hasNextLine()){
            try{
                inputNumbers = scanner.nextLine();//first line of the scenario
                // spliiting user input into appropriate variables
                targetOp = scanner.nextLine();
                operation = targetOp.charAt(targetOp.length() - 1);
                targetOp = targetOp.substring(0, targetOp.length() - 2);
                operation = Character.toUpperCase(operation);
                target = Integer.parseInt(targetOp);

                // convert input numbers into string and removes all spaces
                stringSplitter = null;
                stringSplitter = inputNumbers.split(" ");  
                length = stringSplitter.length;

                // to make sure the array equal to the size of the input numbers
                numbers = null;
                numbers = new int[length];

                // chuck data from the string into the array
                for(i = 0; i < length; i++){
                    numbers[i] = Integer.parseInt(stringSplitter[i]);
                }
            
                ////////////////////////////////////////////////////////
                //Check minimum and maximum
                minimumResult = findminimum (numbers,operation);
                if(minimumResult>target){
                //if the minimum we can get is larger than the target, that means we can't ever reach the target
                    System.out.println(operation + " "+target+" Impossible");
                }else{
                    maximumResult = findmaximum(numbers,operation);
                    if(maximumResult <target){
                        //if maximum is less than the target, that means we can never reach the target either 
                        System.out.println(operation + " "+target+" Impossible");
                    }else{
                        ////////////////////////////////////////////////////////
                        //do the traverse things
                        if(operation == 'L'){
                            found = left_traverse(numbers,target,numbers[0],1,Integer.toString(numbers[0]));
                        }else if(operation == 'N'){
                            //Normal traverse
                            found = norm_traverse(numbers,target,0,1,0,"");
                        }else{
                            System.err.println("ERROR: enter L or N");
                        }

                        if(found!=1){
                            System.out.println(operation + " "+target+" Impossible");
                        }
                        ////////////////////////////////////////////////////////
                    }
                }
            }catch(Exception e){
                System.out.println(e);
                break;
            }
        }
        // Close the scanner, effectively ending the program
        scanner.close();

    }
    //res is the result till the depth and final string is the calculations
    static int left_traverse(int[] numbers,long target,long res,int depth,String finalstring){    
        if(depth == (numbers.length)){
            //return left_traverse(numbers,target,res,depth + 1,finalstring+Integer.toString(numbers[depth]));
            if(res==target){
                System.out.println("L "+ target +" "+ finalstring);
                //System.out.println("there is something wrong");
                return 1;//found
            }
            return 0;//not found
        }else{
            if(res> target){
                return 0;//stop early if too large
            }
        }
        if(left_traverse(numbers,target,res+numbers[depth],depth+1,finalstring+"+"+Integer.toString(numbers[depth]))==1||
           left_traverse(numbers,target,res*numbers[depth],depth+1,finalstring+"*"+Integer.toString(numbers[depth]))==1){
            return 1;
        }else{
            return 0;
        }
    }
    //buffer is to store the curent operation
    static int norm_traverse(int[] numbers,long target,long res,int buffer,int depth,String finalstring){
        if(depth==(numbers.length-1)){
            return norm_traverse(numbers,target,res+(buffer*numbers[depth]),1,depth+1,finalstring+Integer.toString(numbers[depth]));
        }else if(depth==(numbers.length)){
           // System.out.println("N "+ res +" "+ finalstring);
            if(res==target){
                System.out.println("N "+ target +" "+ finalstring);
                return 1;//found
            }
            return 0;//not found
        }else{
            if(res> target){
                return 0;//stop early if too large
            }
            if(norm_traverse(numbers,target,res+(buffer*numbers[depth]),1,depth+1,finalstring+Integer.toString(numbers[depth])+"+")==1 ||
               norm_traverse(numbers,target,res,buffer*numbers[depth],depth+1,finalstring+Integer.toString(numbers[depth])+"*")==1){
                return 1;
            }else{
                return 0;
            }
        }
    }
    static int findminimum(int[] numbers,char mode){
         //Find minimum for left and normal
         int minimum = 0;
            for(int i = 0; i < numbers.length; i++){
                if (numbers[i] ==1){
                    //ignore it
                }
                else{
                    if(minimum ==0){
                        minimum = numbers[i];
                    }else{
                        minimum += numbers[i];
                    }
                }
            }
        return minimum;
    }
   static int findmaximum(int[] numbers,char mode){
        //Find maximum for left and normal 
        int maximum = 0;
        Boolean start = true;
        if(mode=='L'){
            maximum = numbers[0];
            for(int i = 1; i < numbers.length; i++){
                if (numbers[i-1] ==1){
                    maximum += numbers[i];
                }else{
                        maximum *= numbers[i];
                }
            }
        }else if(mode=='N'){
            for(int i=0;i<numbers.length;i++){
                if(numbers[i]==1){
                    if(start){
                        maximum +=1;                 
                    }else{
                        /*pass, maximum * 1*/
                    }
                }else{
                    if(start){
                        start = false;
                        if(maximum==0){
                            maximum = numbers[i];
                        }else{
                            maximum *= numbers[i];
                        }
                    }else{
                        if(maximum==0){
                            maximum = numbers[i];
                        }else{
                            maximum *=numbers[i];
                        }
                    }
                }
            }
            maximum = maximum + 100;/*compensate with inaccuracy*/
        }
        return maximum;
    }
}
