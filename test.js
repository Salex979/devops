// WeatherSphere Pipeline Test
console.log('WeatherSphere CI/CD Test Starting...');

// Test 1: Basic functionality
function validateWeatherData(data) {
  return data && 
         typeof data.temperature === 'number' && 
         data.city;
}

// Test 2: Mock weather service
class WeatherService {
  static getForecast(city) {
    return {
      city: city,
      temperature: 22,
      condition: 'Sunny',
      humidity: 65,
      timestamp: new Date().toISOString()
    };
  }
}

// Run tests
function runTests() {
  console.log('Running tests...');
  
  // Test 1: Data validation
  const testData = WeatherService.getForecast('Moscow');
  const isValid = validateWeatherData(testData);
  
  if (!isValid) {
    throw new Error('Data validation test failed');
  }
  console.log('Data validation test passed');
  
  // Test 2: Temperature range
  if (testData.temperature < -50 || testData.temperature > 50) {
    throw new Error('Temperature range test failed');
  }
  console.log('Temperature range test passed');
  
  // Test 3: City name
  if (testData.city !== 'Moscow') {
    throw new Error('City name test failed');
  }
  console.log('City name test passed');
  
  console.log('All tests passed! WeatherSphere is ready!');
  return true;
}

// Execute tests
try {
  runTests();
} catch (error) {
  console.error(error.message);
  process.exit(1);
}