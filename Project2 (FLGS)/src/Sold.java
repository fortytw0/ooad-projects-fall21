public class Sold {
    public void doAction(Games gameSold, String customerName,CashRegister cashRegister) {
        double income=gameSold.getPrice();
        gameSold.inventory=gameSold.inventory-=1;
        cashRegister.addCash(income);
        System.out.println(customerName+" bought game "+gameSold.getGameName()+" for $"+income);
    }
}
