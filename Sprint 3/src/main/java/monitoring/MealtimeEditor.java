package monitoring;
import java.util.Map;
import java.util.HashMap;

public class MealtimeEditor {
    private String mealtime;
    private int carbToUnitRatio;

    public void updateMealtime(String mealtime, String ratioInput, int fallbackRatio) {
        if (mealtime == null || mealtime.trim().isEmpty()) {
            throw new IllegalArgumentException("Mealtime cannot be empty.");
        }

        int ratio;
        try {
            ratio = Integer.parseInt(ratioInput);
        } catch (NumberFormatException e) {
            ratio = fallbackRatio;
        }

        if (ratio <= 0) {
            throw new IllegalArgumentException("Carb-to-unit ratio must be positive.");
        }

        this.mealtime = mealtime;
        this.carbToUnitRatio = ratio;
    }

    public String getMealtime() {
        return mealtime;
    }

    public int getCarbToUnitRatio() {
        return carbToUnitRatio;
    }

    // Returns dummy meal data for testing the dashboard
    public Map<String, Integer> getUserMeals(String username) {
        Map<String, Integer> meals = new HashMap<>();
        meals.put("Breakfast", 45);
        meals.put("Lunch", 60);
        meals.put("Dinner", 50);
        return meals;
    }

}