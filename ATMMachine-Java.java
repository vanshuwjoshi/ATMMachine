import java.util.Scanner;

class ATM {
    float balance;
    int pin = 7899;

    public void checkPin(){
        System.out.println("Enter your pin: ");
        Scanner sc = new Scanner(System.in);
        int enteredPin = sc.nextInt();
        if(enteredPin==pin){
            menu();
        }
        else{
            System.out.println("Enter a valid pin");
            System.out.println("*********************************");
            checkPin();
        }
        // sc.close();
    }

    public void menu(){
        System.out.println("Enter your choice: ");
        System.out.println("For checking balance press 1");
        System.out.println("For withdrawing money press 2");
        System.out.println("For depositing money press 3");
        System.out.println("To exit press 4");

        Scanner sc = new Scanner(System.in);
        int opt = sc.nextInt();
        // sc.close();

        if(opt==1){
            checkBalance();
        }
        else if(opt==2){
            withdrawMoney();
        }
        else if(opt==3){
            depositMoney();
        }
        else if(opt==4){
            return;
        }
        else{
            System.out.println("Please enter a valid option");
            System.out.println("*********************************");
            menu();
        }
        
    }

    public void checkBalance(){
        System.out.println("Your balance is: $" + balance);
        System.out.println("*********************************");
        menu();
    }

    public void withdrawMoney(){
        System.out.println("Enter amount to withdraw: ");
        Scanner sc = new Scanner(System.in);
        int withdrawAmount = sc.nextInt();
        if(withdrawAmount>balance){
            System.out.println("Insufficient funds");
        }
        else{
            balance = balance - withdrawAmount;
            System.out.println("$"+withdrawAmount+" is withdrawn successfully");
        }
        System.out.println("*********************************");
        menu();
        // sc.close();
    }

    private void depositMoney() {
        System.out.println("Enter amount to deposit: ");
        Scanner sc = new Scanner(System.in);
        int depositAmount = sc.nextInt();
       
        balance = balance + depositAmount;
        System.out.println("$"+depositAmount+" is deposited successfully");
        System.out.println("*********************************");
        menu();
        // sc.close();
    }
}

public class ATMMachine {
    public static void main(String[] args) {
        ATM obj = new ATM();
        obj.checkPin();
    }
}
