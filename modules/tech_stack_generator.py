# modules/tech_stack_generator.py

def suggest_tech_stack(idea):
    idea_lower = idea.lower()

    tech_stack = []
    mvp_idea = ""

    if "mobile" in idea_lower or "app" in idea_lower:
        tech_stack = ["React Native", "Flutter", "Firebase", "Node.js", "MongoDB"]
        mvp_idea = "Develop a cross-platform mobile app using React Native or Flutter, integrate Firebase for authentication and real-time data, and use Node.js with MongoDB for backend services."

    elif "ecommerce" in idea_lower or "shop" in idea_lower or "store" in idea_lower:
        tech_stack = ["Shopify", "Next.js", "Stripe", "MongoDB", "Express.js"]
        mvp_idea = "Create an eCommerce site with product listing, cart, and payment integration using Shopify or build a custom solution using Next.js, Stripe, and MongoDB."

    elif "ai" in idea_lower or "ml" in idea_lower or "machine learning" in idea_lower:
        tech_stack = ["Python", "TensorFlow", "Scikit-learn", "Flask", "PostgreSQL"]
        mvp_idea = "Build an AI-powered backend using Python libraries and serve predictions through Flask APIs with a PostgreSQL database."

    elif "chatbot" in idea_lower:
        tech_stack = ["Dialogflow", "Python", "Flask", "Firebase", "Twilio"]
        mvp_idea = "Use Dialogflow for natural language understanding, and integrate with Flask for custom logic. Deploy it with Firebase or Heroku, and optionally add Twilio for SMS/chat features."

    elif "web" in idea_lower or "website" in idea_lower:
        tech_stack = ["React.js", "Node.js", "Express.js", "MongoDB", "Tailwind CSS"]
        mvp_idea = "Build a responsive website using React for frontend, Node.js/Express.js for backend, and MongoDB for storing data. Use Tailwind for fast UI development."

    else:
        tech_stack = ["HTML", "CSS", "JavaScript", "Python", "SQLite"]
        mvp_idea = "Start with a basic prototype using Python for backend, SQLite for database, and vanilla JavaScript/HTML/CSS for frontend."

    return {
        "stack": tech_stack,
        "mvp": mvp_idea
    }
