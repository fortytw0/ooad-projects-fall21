package com.FLGS.Games;

public class Gloomhaven extends BoardGame{

    public Gloomhaven(){
        super.extraBuyChance = 0.2;
        super.setGameName("Gloomhaven");
        super.setPrice(50.00);
        super.boxLength = 11.50;
        super.boxWidth = 9.10;
        super.boxHeight = 4.50;
        }

    public double getPrice(){
        return this.price;
    }
}

