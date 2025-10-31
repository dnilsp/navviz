# navviz


A Python CLI tool for visualizing navigation endpoints in frontend projects, including React Native Stack Navigator support.

## Features
- Detects project language/framework
- Parses navigation/routes (React, React Native Stack Navigator, extensible to others)
- Extracts screens from React Native Stack Navigator (<Stack.Screen name="..." />)
- Generates navigation graphs (Graphviz/NetworkX)
- Outputs diagrams in-terminal (ASCII/Mermaid) or as PDF

## Usage
```
python -m navviz <project_path> [--output pdf|terminal]
```

### React Native Stack Navigator Example

If your project uses React Navigation's Stack Navigator:

```js
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

function AppNavigator() {
	return (
		<Stack.Navigator initialRouteName="Home">
			<Stack.Screen name="Home" component={HomeScreen} />
			<Stack.Screen name="Details" component={DetailsScreen} />
		</Stack.Navigator>
	);
}
```

navviz will extract the screen names ("Home", "Details") and include them in the navigation graph.

## Requirements
- Python 3.8+
- See requirements.txt for dependencies

## Roadmap
- [x] React/JSX navigation parsing
- [x] React Native Stack Navigator parsing
- [ ] Support for other frameworks/languages
- [ ] PDF and terminal output
- [ ] Modular plugin system
