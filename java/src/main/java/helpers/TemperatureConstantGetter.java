package helpers;


import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class TemperatureConstantGetter {

    private final HttpClient httpClient = HttpClient.newHttpClient();

    public int getHotnessConstant() {
        // We call an external service to get the constant, so first, build the request
        var request = HttpRequest.newBuilder(
                URI.create("https://api.nasa.gov/magicConstantValue1"))
                .header("accept", "application/json")
                .build();

        // Then send the request
        return makeRequest(request);
    }

    public int getHumidityConstant() {
        // We call an external service to get the constant, so first, build the request
        var request = HttpRequest.newBuilder(
                URI.create("https://api.nasa.gov/magicConstantValue2"))
                .header("accept", "application/json")
                .build();

        // Then send the request
        return makeRequest(request);
    }

    private int makeRequest(HttpRequest request) {
        HttpResponse<String> response;
        try {
            response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
            return 0;
        }
        return Integer.getInteger(response.body());
    }
}
