# Day 1 - mental model of AI applications

# A. How an LLM app works
<!-- 
- User inputs a prompt
- Retrievers, if set up, are called. They are chosen based on predefined logic based on user query or through an LLM that acts as a judge to determine which retrievres to call
- Retrievers fetch relevant information from sources (e.g., a SQL database or company manual) and append this information to the users query. They may include additional prompting as well (e.g., you are an expert historian. You answer questions concisely and walk clearly through your reasoning.)
- Updated query is passed to LLM (e.g., Claude, ChatGPT), which generates answer based on its pre-training. Possible to give LLM room to supplement answers with additional info (e.g., web search) if additional context is needed. 
-->

# B. Importance of RAG 
<!-- 
 - Retrieval Augmented Generation is a method for enhancing a prompt with additional information to generate better output from the LLM. At a high level, the benefits are: 
 - Makes 'real time' information retrieval possible, as querying is done when the user prompt is entered so data sources can be updated (vs training data sets, which are static)
 - Reduces hallucination by including  domain specific information in the prompt and grounding the prompt in additional context 
 -->

 # C. Where Agents fit in 
 <!-- 
 - Agents are used to allow the LLM to guide its own processes and tool usage (as opposed to workflows, which follow predefined steps). This allows for handling of ambiguous situations, increasing flexibility and ability to handle open ended problems (at the cost of losing deterministic outputs, increased difficulty troubleshooting, higher risk / lowered predictability)
 - Often we may have a workflow at the macro level (predefined steps) with agents given autonomy within specific sub-tasks (orchestration layer) 
  -->