package pa1.model;

import pa1.util.ReflectionUtils;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class GemTest {

    @Test
    @Tag("sanity")
    @DisplayName("Sanity Test - Public Constructors")
    void testConstructors() {
        final var clazz = Gem.class;
        final var ctors = ReflectionUtils.getPublicConstructors(clazz);

        assertEquals(2, ctors.length);

        assertDoesNotThrow(() -> clazz.getConstructor());
        assertDoesNotThrow(() -> clazz.getConstructor(EntityCell.class));
    }

    @Test
    @Tag("sanity")
    @DisplayName("Sanity Test - Public Methods")
    void testPublicMethods() {
        final var clazz = Gem.class;
        final var publicMethods = ReflectionUtils.getPublicInstanceMethods(clazz);

        assertEquals(2, publicMethods.length);

        assertDoesNotThrow(() -> clazz.getDeclaredMethod("toUnicodeChar"));
        assertDoesNotThrow(() -> clazz.getDeclaredMethod("toASCIIChar"));
    }

    @Test
    @Tag("sanity")
    @DisplayName("Sanity Test - Public Fields")
    void testPublicFields() {
        final var clazz = Gem.class;
        final var publicFields = ReflectionUtils.getPublicInstanceFields(clazz);

        assertEquals(0, publicFields.length);
    }
}
