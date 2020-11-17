import helpers.TemperatureConstantGetter;
import models.ItsFarTooHotException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.stream.Stream;

import static models.Animal.LION;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.anyInt;
import static org.mockito.Mockito.*;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
@ExtendWith(MockitoExtension.class)
class UnitTestingInterviewQuestionsTest {

    // Component under test
    private UnitTestingInterviewQuestions unitTestingInterviewQuestions;

    @BeforeEach
    void beforeEach() {
        var temperatureConstantWrapper = mock(TemperatureConstantGetter.class);
        lenient().when(temperatureConstantWrapper.getHotnessConstant()).thenReturn(10);
        lenient().when(temperatureConstantWrapper.getHumidityConstant()).thenReturn(1);
        unitTestingInterviewQuestions = spy(new UnitTestingInterviewQuestions(temperatureConstantWrapper));
    }

    @Test
    void isItTooHot() throws ItsFarTooHotException {
        doReturn(80).when(unitTestingInterviewQuestions).generateHotnessRating(anyInt(), anyInt());
        assertTrue(unitTestingInterviewQuestions.isItTooHot(10, 10, LION));

        doReturn(50).when(unitTestingInterviewQuestions).generateHotnessRating(anyInt(), anyInt());
        assertFalse(unitTestingInterviewQuestions.isItTooHot(10, 10, LION));
    }

    @ParameterizedTest
    @MethodSource("doComplexHotnessCalculationArguments")
    void doComplexHotnessCalculationTest(int temp, int humidity, int result) {
        assertEquals(result, unitTestingInterviewQuestions.generateHotnessRating(temp, humidity));
    }

    private static Stream<?> doComplexHotnessCalculationArguments() {
        return Stream.of(
                // Test our happy case
                Arguments.of(100, 20, 200),
                // Test a negative temperature
                Arguments.of(-15, 20, -30),
                // Test an 0 value case
                Arguments.of(20, 0, 0)
        );
    }
}