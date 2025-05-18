def record_feedback(query, answer, helpful):
    with open("data/feedback_log.txt", "a") as f:
        f.write(f"QUERY: {query}\nANSWER: {answer}\nHELPFUL: {helpful}\n---\n")
