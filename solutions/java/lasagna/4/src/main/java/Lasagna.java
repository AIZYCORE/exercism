public class Lasagna {
    private static final int EXPECTED_MINUTES_IN_OVEN = 40,
        PREPARATION_MINUTES_PER_LAYER = 2;
    
    public int expectedMinutesInOven(){
        return 40;
    }
    
    public int remainingMinutesInOven(int actualMinutesInOven){
        return expectedMinutesInOven() - actualMinutesInOven;
    }
    
    public int preparationTimeInMinutes(int numberOfTheLayer){
        return numberOfTheLayer * 2;
    }
    
    public int totalTimeInMinutes(int numberOfTheLayer, int theMinutesInOven){
        return  preparationTimeInMinutes(numberOfTheLayer) + theMinutesInOven;
    }
}