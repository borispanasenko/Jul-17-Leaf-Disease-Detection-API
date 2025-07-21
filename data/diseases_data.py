diseases_data = [
    {
        'name': 'Apple___Apple_scab',
        'description': 'Caused by Venturia inaequalis fungus. Dark, velvety spots on leaves turn into scabby lesions. Fruits develop dark, rough patches, often cracking.',
        'treatment': 'Apply sulfur or captan fungicides every 7-10 days during wet seasons. Use resistant varieties (e.g., Enterprise, Liberty). Remove fallen leaves. Prune for air circulation.'
    },
    {
        'name': 'Apple___Black_rot',
        'description': 'Caused by Botryosphaeria obtusa. Black, irregularly shaped lesions on leaves; fruits show brown-to-black rot with concentric rings, often at blossom end.',
        'treatment': 'Apply captan or myclobutanil fungicides. Prune infected branches, remove mummified fruits. Use resistant varieties. Sanitize tools to prevent spread.'
    },
    {
        'name': 'Apple___Cedar_apple_rust',
        'description': 'Caused by Gymnosporangium juniperi-virginianae. Yellow-orange spots with black centers on leaves, often with red halo. Fruits may have small lesions.',
        'treatment': 'Apply myclobutanil or sulfur fungicides from bud break to petal fall. Remove nearby cedar/juniper hosts. Use resistant varieties (e.g., Freedom).'
    },
    {
        'name': 'Apple___healthy',
        'description': 'Healthy apple leaves are green, smooth, free of spots or lesions. Fruits are unblemished, uniform in color.',
        'treatment': 'No treatment needed. Regular pruning, balanced fertilization, and pest monitoring maintain health. Avoid overhead watering.'
    },
    {
        'name': 'Blueberry___healthy',
        'description': 'Healthy blueberry leaves are vibrant green, glossy, with no spots or wilting. Berries are plump, evenly colored.',
        'treatment': 'No treatment needed. Maintain acidic soil (pH 4.5-5.5), use drip irrigation, and monitor for pests.'
    },
    {
        'name': 'Cherry_(including_sour)___Powdery_mildew',
        'description': 'Caused by Podosphaera clandestina. White, powdery coating on leaves, stems, or fruits. Leaves may yellow and drop prematurely.',
        'treatment': 'Apply sulfur or potassium bicarbonate fungicides. Prune for air circulation. Avoid excessive nitrogen fertilizer. Remove infected debris.'
    },
    {
        'name': 'Cherry_(including_sour)___healthy',
        'description': 'Healthy cherry leaves are dark green, glossy, with no spots or wilting. Fruits are smooth, vibrant.',
        'treatment': 'No treatment needed. Prune annually, use drip irrigation, and monitor for pests and early disease signs.'
    },
    {
        'name': 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
        'description': 'Caused by Cercospora zeae-maydis. Rectangular, grayish-tan lesions with wavy edges on leaves, often along veins. Severe cases cause leaf death.',
        'treatment': 'Apply azoxystrobin or propiconazole fungicides. Use resistant hybrids (e.g., Pioneer hybrids). Rotate crops, remove debris.'
    },
    {
        'name': 'Corn_(maize)___Common_rust',
        'description': 'Caused by Puccinia sorghi. Orange to brown pustules scattered on leaves, leading to reduced photosynthesis. Severe cases cause leaf necrosis.',
        'treatment': 'Apply triazole or strobilurin fungicides (e.g., Tilt) early. Use resistant varieties. Avoid dense planting, ensure good air flow.'
    },
    {
        'name': 'Corn_(maize)___Northern_Leaf_Blight',
        'description': 'Caused by Exserohilum turcicum. Long, cigar-shaped, gray-green lesions on leaves, turning tan or brown. Can cause significant yield loss.',
        'treatment': 'Apply propiconazole or mancozeb fungicides. Use resistant hybrids. Rotate crops, plow under residue to reduce inoculum.'
    },
    {
        'name': 'Corn_(maize)___healthy',
        'description': 'Healthy corn leaves are dark green, smooth, with no spots or lesions. Stalks and ears develop normally.',
        'treatment': 'No treatment needed. Use balanced fertilization, monitor soil moisture, and scout for early disease signs.'
    },
    {
        'name': 'Grape___Black_rot',
        'description': 'Caused by Guignardia bidwellii. Black spots on leaves with yellow halos; berries develop brown, shriveled lesions, turning black and mummified.',
        'treatment': 'Apply myclobutanil or captan fungicides from bud break to veraison. Remove infected berries and debris. Prune for air circulation.'
    },
    {
        'name': 'Grape___Esca_(Black_Measles)',
        'description': 'Caused by Phaeoacremonium and Phaeomoniella fungi. Tiger-stripe patterns on leaves, black lesions on berries, and wood decay in vines.',
        'treatment': 'No effective chemical control. Prune out infected wood, sanitize tools. Use resistant rootstocks. Avoid water stress.'
    },
    {
        'name': 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
        'description': 'Caused by Pseudocercospora vitis. Dark brown to black spots with yellow margins on leaves, leading to defoliation in severe cases.',
        'treatment': 'Apply captan or sulfur fungicides. Remove fallen leaves. Prune for better air circulation. Avoid overhead irrigation.'
    },
    {
        'name': 'Grape___healthy',
        'description': 'Healthy grape leaves are green, glossy, with no spots or discoloration. Berries develop uniformly.',
        'treatment': 'No treatment needed. Prune annually, use drip irrigation, and monitor for pests and diseases.'
    },
    {
        'name': 'Orange___Haunglongbing_(Citrus_greening)',
        'description': 'Caused by Candidatus Liberibacter bacteria. Yellowing leaves with blotchy mottle, small, misshapen fruits with bitter taste.',
        'treatment': 'No cure. Remove infected trees to prevent spread. Use disease-free nursery stock. Control psyllid vectors with insecticides (e.g., imidacloprid).'
    },
    {
        'name': 'Peach___Bacterial_spot',
        'description': 'Caused by Xanthomonas campestris pv. pruni. Small, water-soaked spots on leaves turn dark brown/black, often with yellow halo. Fruits show pitting.',
        'treatment': 'Apply copper-based bactericides (e.g., Kocide) early season. Use resistant varieties (e.g., Contender). Remove infected debris, avoid overhead watering.'
    },
    {
        'name': 'Peach___healthy',
        'description': 'Healthy peach leaves are bright green, smooth, with no spots. Fruits are uniform, blemish-free.',
        'treatment': 'No treatment needed. Prune for structure, fertilize moderately, and monitor for pests.'
    },
    {
        'name': 'Pepper,_bell___Bacterial_spot',
        'description': 'Caused by Xanthomonas campestris pv. vesicatoria. Dark, water-soaked spots on leaves and fruits, turning black with yellow halos. Leaf drop possible.',
        'treatment': 'Apply copper-based bactericides (e.g., copper hydroxide). Use resistant varieties (e.g., Revolution). Remove debris, rotate crops.'
    },
    {
        'name': 'Pepper,_bell___healthy',
        'description': 'Healthy bell pepper leaves are dark green, glossy, with no spots. Fruits are smooth, vibrant.',
        'treatment': 'No treatment needed. Maintain even watering, fertilize with balanced nutrients, and scout for pests.'
    },
    {
        'name': 'Potato___Early_blight',
        'description': 'Caused by Alternaria solani. Dark brown spots with concentric rings ("bull’s-eye") on lower leaves, yellowing around spots, leading to defoliation.',
        'treatment': 'Apply chlorothalonil or mancozeb fungicides every 7-14 days. Use resistant varieties (e.g., Defender). Rotate crops, remove debris.'
    },
    {
        'name': 'Potato___Late_blight',
        'description': 'Caused by Phytophthora infestans. Irregular, water-soaked lesions on leaves, turning brown/black. White mold on leaf undersides in humid conditions.',
        'treatment': 'Apply chlorothalonil or copper fungicides (e.g., Dithane). Use resistant varieties (e.g., Kennebec). Destroy infected tubers, avoid overhead watering.'
    },
    {
        'name': 'Potato___healthy',
        'description': 'Healthy potato leaves are green, smooth, with no spots or wilting. Tubers develop normally.',
        'treatment': 'No treatment needed. Use certified seed potatoes, rotate crops, and monitor soil health.'
    },
    {
        'name': 'Raspberry___healthy',
        'description': 'Healthy raspberry leaves are green, free of spots or discoloration. Canes and berries develop normally.',
        'treatment': 'No treatment needed. Prune old canes, use drip irrigation, and monitor for pests like spider mites.'
    },
    {
        'name': 'Soybean___healthy',
        'description': 'Healthy soybean leaves are green, trifoliate, with no spots or yellowing. Pods are plump and uniform.',
        'treatment': 'No treatment needed. Maintain soil fertility, use crop rotation, and scout for early disease signs.'
    },
    {
        'name': 'Squash___Powdery_mildew',
        'description': 'Caused by Podosphaera xanthii. White, powdery spots on leaves and stems, spreading to cover foliage. Leaves may yellow and die.',
        'treatment': 'Apply sulfur or myclobutanil fungicides early. Use resistant varieties (e.g., Success PM). Improve air circulation, avoid overhead watering.'
    },
    {
        'name': 'Strawberry___Leaf_scorch',
        'description': 'Caused by Diplocarpon earlianum. Dark purple to black spots on leaves, merging into large scorched areas. Leaves may dry and curl.',
        'treatment': 'Apply captan or sulfur fungicides. Remove infected leaves, improve air circulation. Use resistant varieties (e.g., Chandler).'
    },
    {
        'name': 'Strawberry___healthy',
        'description': 'Healthy strawberry leaves are bright green, glossy, with no spots. Fruits are red, uniform, and blemish-free.',
        'treatment': 'No treatment needed. Mulch with straw, use drip irrigation, and monitor for pests like slugs.'
    },
    {
        'name': 'Tomato___Bacterial_spot',
        'description': 'Caused by Xanthomonas campestris pv. vesicatoria. Small, water-soaked spots on leaves turn dark brown/black with yellow halos. Fruits show raised lesions.',
        'treatment': 'Apply copper-based bactericides (e.g., Kocide). Use resistant varieties (e.g., Mountain Fresh). Remove debris, avoid overhead watering.'
    },
    {
        'name': 'Tomato___Early_blight',
        'description': 'Caused by Alternaria solani. Dark brown spots with concentric rings ("bull’s-eye") on lower leaves, yellowing around spots, causing leaf drop.',
        'treatment': 'Apply chlorothalonil or mancozeb fungicides every 7-14 days. Use resistant varieties (e.g., Mountain Magic). Rotate crops, mulch soil.'
    },
    {
        'name': 'Tomato___Late_blight',
        'description': 'Caused by Phytophthora infestans. Irregular, water-soaked lesions on leaves, turning brown/black. White mold on undersides in humid conditions.',
        'treatment': 'Apply chlorothalonil or copper fungicides (e.g., Dithane). Use resistant varieties (e.g., Mountain Magic). Destroy infected plants, use drip irrigation.'
    },
    {
        'name': 'Tomato___Leaf_Mold',
        'description': 'Caused by Passalora fulva. Yellow spots on upper leaf surfaces, grayish-white mold on undersides. Leaves may curl and drop.',
        'treatment': 'Apply chlorothalonil or maneb fungicides. Increase air circulation, use resistant varieties (e.g., Plum Regal). Avoid high humidity.'
    },
    {
        'name': 'Tomato___Septoria_leaf_spot',
        'description': 'Caused by Septoria lycopersici. Small, circular spots with gray centers and dark margins on lower leaves. Black fruiting bodies in centers.',
        'treatment': 'Apply chlorothalonil or copper fungicides. Remove affected leaves, rotate crops, use drip irrigation. No fully resistant varieties.'
    },
    {
        'name': 'Tomato___Spider_mites Two-spotted_spider_mite',
        'description': 'Caused by Tetranychus urticae. Tiny yellow-white stippling on leaves, fine webbing on undersides. Leaves may bronze and drop.',
        'treatment': 'Apply miticides (e.g., abamectin) or insecticidal soap. Increase humidity, spray water to disrupt mites. Introduce predatory mites.'
    },
    {
        'name': 'Tomato___Target_Spot',
        'description': 'Caused by Corynespora cassiicola. Small, dark brown spots with yellow halos on leaves, expanding to large lesions. Fruits show sunken spots.',
        'treatment': 'Apply azoxystrobin or chlorothalonil fungicides. Remove infected leaves, rotate crops. Avoid overhead watering.'
    },
    {
        'name': 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
        'description': 'Caused by TYLCV (virus). Upward leaf curling, yellowing, stunted growth. Fruits small, reduced yield.',
        'treatment': 'No cure. Remove infected plants. Control whitefly vectors with insecticides (e.g., imidacloprid). Use resistant varieties (e.g., Tycoon).'
    },
    {
        'name': 'Tomato___Tomato_mosaic_virus',
        'description': 'Caused by ToMV. Mottled green-yellow leaves, mosaic patterns, stunted growth. Fruits may have uneven ripening.',
        'treatment': 'No cure. Remove infected plants, sanitize tools. Use resistant varieties (e.g., Celebrity). Avoid handling plants when wet.'
    },
    {
        'name': 'Tomato___healthy',
        'description': 'Healthy tomato leaves are vibrant green, smooth, with no spots or wilting. Fruits are uniform, blemish-free.',
        'treatment': 'No treatment needed. Use drip irrigation, balanced fertilization, and monitor for early disease signs.'
    }
]