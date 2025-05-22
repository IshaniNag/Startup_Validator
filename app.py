# import streamlit as st
# from modules.nlp_analysis import extract_keywords
# from modules.sentiment_analysis import analyze_sentiment
# from modules.trend_checker import get_trend_scores
# from modules.similar_startups import find_similar_startups
# from modules.scoring import calculate_score
# from modules.improvement_generator import generate_improvements
# from modules.tech_stack_generator import suggest_tech_stack
# from modules.pdf_export import convert_html_to_pdf
# from modules.scoring import calculate_score, explain_score

# def main():
#     st.set_page_config(page_title="Startup Idea Validator", layout="wide")
#     st.title("🚀 Startup Idea Validator")
#     st.markdown("Validate your startup idea using AI and market insights.")

#     idea = st.text_area("💡 Describe your startup idea", height=200)

#     if st.button("Validate"):
#         if not idea.strip():
#             st.warning("Please enter a startup idea.")
#             return

#         with st.spinner("Analyzing your idea..."):

#             # Step 1: Extract Keywords
#             keywords = extract_keywords(idea)
#             st.subheader("🔑 Extracted Keywords")
#             st.write(keywords)

#             # Step 2: Sentiment Analysis
#             sentiment_score = analyze_sentiment(idea)
#             st.subheader("😊 Sentiment Score")
#             st.write(f"{sentiment_score:.2f} (−1 = Negative, +1 = Positive)")

#             # Step 3: Trend Analysis
#             trend_scores = get_trend_scores(keywords)
#             st.subheader("📈 Trend Scores")
#             st.write(trend_scores)

#             # Step 4: Similar Startups
#             similar = []
#             for keyword in keywords:
#                 similar.extend(find_similar_startups(str(keyword)))
#             st.subheader("🔍 Similar Startups")
#             if similar:
#                 for s in similar:
#                     st.markdown(f"- [{s['name']}]({s['url']})")
#             else:
#                 st.write("No direct competitors found!")

#             # Step 5: Scoring
#             score = calculate_score(idea, sentiment_score, trend_scores)
#             st.subheader("🏆 Validation Score")
#             st.write(f"Your startup idea scores **{score}/100**.")
#             explanation = explain_score(idea)
#             st.markdown(f"**Why this score?** {explanation}")

#             # Step 6: Tech Stack
#             tech_info = suggest_tech_stack(idea)
#             st.subheader("🧰 Suggested Tech Stack")
#             for tech in tech_info.get('stack', []):
#                  st.write(f"- {tech}")
#             st.markdown(f"**MVP Idea:** {tech_info.get('mvp', 'Not available')}")


#             # Step 7: Improvement Suggestions
#             st.subheader("🛠️ Suggestions to Improve")
#             try:
#                 improvements = generate_improvements(idea)
#                 st.write(improvements)
#             except Exception as e:
#                 st.warning("Improvement generator failed.")
#                 st.error(str(e))
#                 improvements = "N/A"

#             # Step 8: Export to PDF
#             result_data = {
#                 "Startup Idea": idea,
#                 "Keywords": keywords,
#                 "Sentiment Score": sentiment_score,
#                 "Trend Scores": trend_scores,
#                 "Similar Startups": [s["name"] for s in similar],
#                 "Validation Score": score,
#                 "Suggested Tech Stack": tech_info.get('stack', []),
#                 "MVP Idea": tech_info.get('mvp', 'Not available'),
#                 "Improvement Suggestions": improvements
#             }
#             # HTML string for the report (you can make this prettier)
#             html_content = f"""
#             <h1>🚀 Startup Idea Report</h1>
#             <p><strong>Idea:</strong> {idea}</p>
#             <p><strong>Keywords:</strong> {keywords}</p>
#             <p><strong>Sentiment Scores:</strong> {sentiment_score}</p>
#             <p><strong>Trend Scores:</strong> {trend_scores}</p>
#             <p><strong>Similar Startups:</strong> {similar}</p>
#             <p><strong>Validation Score:</strong>{score}</p>
#             <p><strong>Suggest Tech Stack:</strong>{tech_info}</p>
#             <p><strong>Suggestiongs to Improve:</strong>{improvements}</p>
#             """

#             # Convert to PDF
#             pdf = convert_html_to_pdf(html_content)
#             # Download button
#             if pdf:
#                 st.download_button(
#                     label="📄 Download Report as PDF",
#                     data=pdf,
#                     file_name="startup_report.pdf",
#                     mime="application/pdf"
#                     )

# if __name__ == "__main__":
#     main()

import streamlit as st
from modules.nlp_analysis import extract_keywords
from modules.sentiment_analysis import analyze_sentiment
from modules.trend_checker import get_trend_scores
from modules.similar_startups import find_similar_startups
from modules.scoring import calculate_score, explain_score
from modules.improvement_generator import generate_improvements
from modules.tech_stack_generator import suggest_tech_stack
from modules.pdf_export import convert_html_to_pdf
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    st.set_page_config(page_title="Startup Idea Validator", layout="wide")

    # Sidebar
    with st.sidebar:
        lottie_animation = load_lottie_url("https://lottie.host/c1b97304-6264-422f-be3e-a698a42f4271/Pbtf9Yne5i.json")
        if lottie_animation:
            st_lottie(lottie_animation, height=200)
        st.markdown("## 👩‍💻 Startup Validator")
        st.markdown("Validate your idea with AI-powered insights!")
        st.markdown("---")
        st.markdown("✨ Made by Stuti (71), Shruti (72), Ishani (75) and Saniya (86) ✨")

    # Header section
    st.title("🏢 Startup Idea Validator")
    st.markdown("""
        <div style="background-color:#f0f2f6;padding:10px 20px;border-radius:10px">
            <h3 style="color:#333;">✨ Instantly validate your startup idea using NLP, sentiment & trend analysis</h3>
        </div>
        """, unsafe_allow_html=True)

    # Lottie animation
    lottie_startup = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")
    if lottie_startup:
        st_lottie(lottie_startup, height=200)

    # Input box
    idea = st.text_area("💡 Describe your startup idea", height=200, placeholder="e.g., An AI tool to summarize online lectures for students")

    if st.button("🚀 Validate"):
        if not idea.strip():
            st.warning("Please enter a startup idea.")
            return

        with st.spinner("Analyzing your idea..."):

            # Step 1: Extract Keywords
            keywords = extract_keywords(idea)

            # Step 2: Sentiment Analysis
            sentiment_score = analyze_sentiment(idea)

            # Step 3: Trend Analysis
            trend_scores = get_trend_scores(keywords)

            # Step 4: Similar Startups
            similar = []
            for keyword in keywords:
                similar.extend(find_similar_startups(str(keyword)))

            # Step 5: Scoring
            score = calculate_score(idea, sentiment_score, trend_scores)
            explanation = explain_score(idea)

            # Step 6: Tech Stack
            tech_info = suggest_tech_stack(idea)

            # Step 7: Improvements
            try:
                improvements = generate_improvements(idea)
            except Exception as e:
                st.warning("Improvement generator failed.")
                st.error(str(e))
                improvements = "N/A"

            # Display Results
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🔑 Extracted Keywords")
                st.write(keywords)

                st.subheader("😊 Sentiment Score")
                st.write(f"{sentiment_score:.2f} (−1 = Negative, +1 = Positive)")

                st.subheader("🧰 Suggested Tech Stack")
                for tech in tech_info.get('stack', []):
                    st.write(f"- {tech}")
                st.markdown(f"**MVP Idea:** {tech_info.get('mvp', 'Not available')}")

            with col2:
                st.subheader("📈 Trend Scores")
                st.write(trend_scores)

                st.subheader("🏆 Validation Score")
                st.write(f"Your startup idea scores **{score}/100**.")
                st.markdown(f"**Why this score?** {explanation}")

            with st.expander("🔍 View Similar Startups"):
                if similar:
                    for s in similar:
                        st.markdown(f"- [{s['name']}]({s['url']})")
                else:
                    st.write("No direct competitors found!")

            with st.expander("🛠️ Suggestions to Improve"):
                st.write(improvements)

            # PDF Export
            result_data = {
                "Startup Idea": idea,
                "Keywords": keywords,
                "Sentiment Score": sentiment_score,
                "Trend Scores": trend_scores,
                "Similar Startups": [s["name"] for s in similar],
                "Validation Score": score,
                "Suggested Tech Stack": tech_info.get('stack', []),
                "MVP Idea": tech_info.get('mvp', 'Not available'),
                "Improvement Suggestions": improvements
            }

            html_content = f"""
                <h1>🚀 Startup Idea Report</h1>
                <p><strong>Idea:</strong> {idea}</p>
                <p><strong>Keywords:</strong> {keywords}</p>
                <p><strong>Sentiment Scores:</strong> {sentiment_score}</p>
                <p><strong>Trend Scores:</strong> {trend_scores}</p>
                <p><strong>Similar Startups:</strong> {[s['name'] for s in similar]}</p>
                <p><strong>Validation Score:</strong> {score}</p>
                <p><strong>Suggested Tech Stack:</strong> {tech_info.get('stack', [])}</p>
                <p><strong>MVP Idea:</strong> {tech_info.get('mvp')}</p>
                <p><strong>Suggestions to Improve:</strong> {improvements}</p>
            """

            pdf = convert_html_to_pdf(html_content)
            if pdf:
                with st.container():
                    st.success("✅ Analysis complete! Download your report below.")
                    st.download_button(
                        label="📄 Download Report as PDF",
                        data=pdf,
                        file_name="startup_report.pdf",
                        mime="application/pdf"
                    )

if __name__ == "__main__":
    main()

