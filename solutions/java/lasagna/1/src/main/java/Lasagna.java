public class Lasagna {
    // TODO: define the 'expectedMinutesInOven()' method

    // TODO: define the 'remainingMinutesInOven()' method

    // TODO: define the 'preparationTimeInMinutes()' method

    // TODO: define the 'totalTimeInMinutes()' method

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
