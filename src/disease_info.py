DISEASE_INFO = {
    "Melanoma": {
        "description": "Melanoma is a serious form of skin cancer that begins in cells known as melanocytes. It is less common than other skin cancers but is more dangerous because of its ability to spread rapidly to other organs if not treated early.",
        "precautions": [
            "Seek immediate medical consultation from a qualified dermatologist.",
            "Perform regular self-examinations using the ABCDE guide.",
            "Protect your skin from UV radiation with sunscreen, protective clothing, and shade.",
            "Avoid tanning beds and artificial UV exposure."
        ]
    },
    "Melanocytic Nevi": {
        "description": "Melanocytic Nevi (commonly known as moles) are benign, non-cancerous growths on the skin caused by clusters of melanocytes. While usually harmless, they should be monitored for any structural, color, or size changes that may indicate dysplastic behavior.",
        "precautions": [
            "Monitor for changes in size, shape, color, or elevation.",
            "Have a yearly skin check by a dermatologist.",
            "Protect skin from excessive sun exposure.",
            "Avoid picking, scratching, or attempting to remove moles yourself."
        ]
    },
    "Benign Keratosis": {
        "description": "Benign Keratosis-like lesions (including seborrheic keratosis, solar lentigines, and lichen-planus like keratoses) are non-cancerous skin growths common in older adults. They often appear waxy, scaly, or slightly elevated, with color ranging from tan to black.",
        "precautions": [
            "Consult a doctor to confirm diagnosis and rule out malignancy.",
            "Avoid scratching or rubbing the lesion to prevent irritation or secondary infection.",
            "Wear sunscreen and protective wear to minimize solar damage.",
            "Consider removal via cryotherapy or curettage if requested for cosmetic reasons."
        ]
    },
    "Basal Cell Carcinoma": {
        "description": "Basal Cell Carcinoma (BCC) is the most common form of skin cancer. It typically develops in areas exposed to the sun, such as the face and neck. It grows slowly and rarely metastasizes, but can cause significant local damage if left untreated.",
        "precautions": [
            "Schedule a dermatologist appointment for evaluation and biopsy.",
            "Limit direct exposure to mid-day sun.",
            "Apply broad-spectrum sunscreen with SPF 30 or higher daily.",
            "Explore treatment options, such as surgical excision, Mohs surgery, or topical medications."
        ]
    },
    "Actinic Keratosis": {
        "description": "Actinic Keratosis (AK) is a rough, scaly patch on the skin caused by years of sun exposure. It is classified as a pre-cancerous lesion because it can develop into squamous cell carcinoma if left untreated.",
        "precautions": [
            "Schedule a dermatological assessment to treat pre-cancerous lesions.",
            "Use prescription topical treatments, cryotherapy, or photodynamic therapy as advised.",
            "Apply high-protection sunscreen daily and avoid direct sunlight.",
            "Regularly inspect skin for new rough or scaly patches."
        ]
    },
    "Vascular Lesion": {
        "description": "Vascular lesions (such as cherry angiomas, angiokeratomas, pyogenic granulomas) are common skin growths that contain an abnormally high concentration of blood vessels. Most vascular lesions are benign and do not require treatment unless they bleed, hurt, or are cosmetically bothersome.",
        "precautions": [
            "Consult a medical practitioner to rule out other conditions.",
            "Avoid scratching or puncture to prevent bleeding.",
            "Seek professional treatment (laser therapy, cryosurgery, or excision) if removal is desired.",
            "Monitor for sudden changes in size, shape, or color."
        ]
    },
    "Dermatofibroma": {
        "description": "Dermatofibroma is a common, benign, firm skin nodule that typically develops on the lower legs. They are usually harmless and composed of fibrous tissue, often developing after a minor injury like an insect bite or nick from shaving.",
        "precautions": [
            "Ensure correct professional diagnosis to avoid confusion with malignant tumors.",
            "Avoid trying to squeeze or cut the nodule.",
            "Monitor for sudden growth, bleeding, or color changes.",
            "Consider surgical removal only if it is symptomatic (itchy, painful) or subject to repeated irritation."
        ]
    }
}

# Automatically add underscored and lowercase aliases for robust matching
for key in list(DISEASE_INFO.keys()):
    # Underscored alias
    underscored = key.replace(" ", "_")
    if underscored != key:
        DISEASE_INFO[underscored] = DISEASE_INFO[key]
    
    # Lowercase alias
    lowercase = key.lower()
    if lowercase != key:
        DISEASE_INFO[lowercase] = DISEASE_INFO[key]

    # Lowercase underscored alias
    lowercase_underscored = underscored.lower()
    if lowercase_underscored != key:
        DISEASE_INFO[lowercase_underscored] = DISEASE_INFO[key]
