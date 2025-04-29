package monitoring;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.Map;

public class MealtimeEditor {
    private static final String MEALTIME_FILE = "src/main/resources/mealtimes.json";
    private final Gson gson = new Gson();

    // Loads the entire mealtime file as a Map<username, Map<meal, Map<time/ratio, value>>>
    private Map<String, Map<String, Map<String, String>>> loadMealtimes() {
        try (Reader reader = new FileReader(MEALTIME_FILE)) {
            Type type = new TypeToken<Map<String, Map<String, Map<String, String>>>>() {}.getType();
            Map<String, Map<String, Map<String, String>>> mealtimes = gson.fromJson(reader, type);
            return (mealtimes != null) ? mealtimes : new HashMap<>();
        } catch (IOException e) {
            return new HashMap<>();
        }
    }

    // Saves the full structure back to file
    private void saveMealtimes(Map<String, Map<String, Map<String, String>>> mealtimes) {
        try (Writer writer = new FileWriter(MEALTIME_FILE)) {
            gson.toJson(mealtimes, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void updateMealtime(String username, String meal, String time, int carbToUnitRatio) {
        Map<String, Map<String, Map<String, String>>> mealtimes = loadMealtimes();
        mealtimes.putIfAbsent(username, new HashMap<>());
        Map<String, Map<String, String>> userMeals = mealtimes.get(username);

        Map<String, String> mealData = new HashMap<>();
        mealData.put("time", time);
        mealData.put("carbToUnitRatio", String.valueOf(carbToUnitRatio));
        userMeals.put(meal.toLowerCase(), mealData);

        saveMealtimes(mealtimes);
    }

    public Map<String, Map<String, String>> getUserMeals(String username) {
        Map<String, Map<String, Map<String, String>>> mealtimes = loadMealtimes();
        return mealtimes.getOrDefault(username, new HashMap<>());
    }
}
