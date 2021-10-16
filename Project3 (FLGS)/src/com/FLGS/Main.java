package com.FLGS;
import com.FLGS.Games.*;
import com.FLGS.Store.CashRegister;
import com.FLGS.Store.Store;
import com.FLGS.Store.Wares;
import com.FLGS.Utils.RandomUtils;

import java.io.FileNotFoundException;

public class Main {

    public static Store store = new Store();
    public static CashRegister register = new CashRegister();
    public static Wares wares = new Wares();

    public static void main(String[] args) throws FileNotFoundException {

        store.simulate(3);
    }
}
