import string
import os
import site
import sys
import os
import json
import predictionguard as pg
from getpass import getpass
import predictionguard as pg
from sentence_transformers import SentenceTransformer
import faiss
os.environ['PREDICTIONGUARD_TOKEN'] = "q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E"
knowledge_base = [
    "Important About Sustainability: As consumers become more environmentally conscious, more companies and businesses are finding ways to reduce their impacts upon the planet and their community. Sustainability practices allow companies to highlight their social benefits while continuing to attract customers.",
    "Fun Fact 1: It takes more energy to make 1 kg of paper than it takes to make 1 kg of steel.",
    "Fun Fact 2: It takes almost 500,000 litres of water to extract just 1 kg of gold",
    "Sustainability is ability to maintain or support a process over time.",
    "Sustainability is often broken into three core concepts: economic, environmental, and social.",
    "Many businesses and governments have committed to sustainable goals, such as reducing their environmental footprints and conserving resources.",
    "3 Pillars of Sustainability: The idea of sustainability is often broken down into three pillars: economic, environmental, and social—also known informally as profits, planet, and people. In that breakdown, the concept of economic sustainability focuses on conserving the natural resources that provide physical inputs for economic production, including both renewable and exhaustible inputs. The concept of environmental sustainability adds greater emphasis on the life support systems, such as the atmosphere or soil, that must be maintained for economic production or human life to even occur. In contrast, social sustainability focuses on the human effects of economic systems, and the category includes attempts to eradicate poverty and hunger, as well as to combat inequality. In 1983, the United Nations created the World Commission on Environment and Development to study the connection between ecological health, economic development, and social equity. The commission, then run by former Norwegian prime minister Gro Harlem Brundtland, published a report in 1987 that has become the standard in defining sustainable development. That report describes sustainable development, or the blueprint for attaining sustainability, as meeting the needs of the present without compromising the ability of future generations to meet their own needs.",
    "Corporate Sustainability: In business contexts, sustainability refers to more than just environmentalism. Harvard Business School lists two ways to measure sustainable business practices: the effect a business has on the environment, and the effect a business has on society, with the goal of sustainable practice being to have a positive impact on at least one of those areas. This view of responsibility encourages businesses to balance long-term benefits with immediate returns, and the goal of pursuing inclusive and environmentally sound objectives. This covers a broad array of possible practices. Cutting emissions, lowering energy usage, sourcing products from fair-trade organizations, and ensuring their physical waste is disposed of properly and with a smaller carbon footprint would qualify as moves toward sustainability. Companies have also set sustainability goals such as a commitment to zero-waste packaging by a certain year, or to reduce overall emissions by a certain percentage. Many corporations have made such sustainability promises in recent years. For example, Walmart Stores, Inc. has pledged to reach zero emissions by 2040. Morgan Stanley has pledged net-zero financed emissions by 2050. Google has pledged to operate carbon-free by 2030. The push for sustainability is evident in areas such as energy generation as well, where the focus has been on finding new deposits to outpace the drawdown on existing reserves. Some electricity companies, for example, now publicly state goals for energy generation from sustainable sources such as wind, hydropower, and solar. Because these policies tend to generate public goodwill, some companies have been accused of greenwashing, the practice of providing a false impression that makes a business seem more environmentally friendly than it is.",
    "Cost Cutting: Moreover, many companies have been criticized for cost-cutting measures that make it harder to evaluate their sustainability. For example, many companies might move some parts of their business to less-regulated markets, such as by offshoring production to obtain cheaper labor. This can make it harder to assess the costs of production on workers and the environment. Sustainability practices significantly affect the offshoring activities of multinational corporations, according to an examination of data from 1,080 multinational corporations.",
    "Challenges Surrounding Business Sustainability: The switch to sustainability can be difficult. The Santa Fe Institute outlines three major impediments for firms seeking to improve their environmental impacts: First, it is hard to actually understand the impact of any individual firm. Second, it is difficult to rank the environmental impact of some activities, and finally, it is difficult to predict how economic agents respond to changing incentives. Sustainable investing surveys over the past couple of years have suggested that half (or in some cases, more than half) of investors say that sustainability is fundamental to investing strategy. Not everyone concerned with investments shares the enthusiasm. In July 2021, for instance, Securities and Exchange Commission (SEC) Commissioner Hester Peirce argued that not only would environmental, social, and governance (ESG) disclosure mandates violate the agency's authority, but it may also undermine financial and economic stability. According to Peirce, the inherently political sustainability metrics were unabashedly created to direct capital toward certain businesses. In response to public comments and regulatory pressure to look into such mandates, Peirce said that it would be a violation of the SEC's historically agnostic approach to regulations. Eiji Hirano, a former chairman of the board of visitors for Japans Government Pension Investment Fund, has said that there's a bubble in ESG investing and that the fund needs to rethink its ESG investments, according to interviews with Bloomberg News.",
    "Benefits of Business Sustainability: In addition to the social benefits of improving the environment and elevating human needs, there are also financial benefits for companies that successfully implement sustainability strategies. Using resources sustainability can improve the long-term viability of a business concern, just as cutting waste and pollution can also help a company save money. For example, using more efficient lighting and plumbing fixtures can help a company save on utility bills, as well as improve its public image. There may also be government tax incentives for companies that adopt certain sustainability practices. Sustainability can also make a company more attractive to investors. A 2019 HEC Paris Research paper showed that shareholders value the ethical dimensions of a firm so much that they are willing to pay $.70 more to purchase a share in a firm that gives a dollar or more per share to charities. The study also revealed a loss in valuation for firms perceived as exercising a negative social impact. Based on interviews with senior executives across 43 global investing firms, Harvard Business Review has argued that the perception among some business leaders that environmental, social, and governance issues are not mainstream in the investment community is outdated. The sea change in investor attitudes described by Harvard Business Review draws on the increased commitments of investors. The Principles for Responsible Investment, a United Nations-supported effort to bring these issues into investing, had 63 investment companies with $6.5 trillion in assets under management that committed when it launched in 2006. In 2018, it had 1,715 companies with $81.7 trillion in assets.",
    "Warning: While it's tempting to support companies that seem environmentally friendly, some companies are less sustainable than they seem. This use of misleading advertisements or branding to create a false impression of sustainability is sometimes called greenwashing.",
    "Creating a Sustainable Business Strategy: Many corporations are seeking to integrate sustainability practices into their core business models. Companies can adopt sustainability strategies in the same way that they develop their other strategic plans. The first step to integrating sustainability practices is to identify a specific weakness shortcoming. For example, a company might determine that it generates too much waste, or that its hiring practices are causing harm to the surrounding communities. Next, the company should determine its goals, and identify the metrics it will use to measure its achievements. A company might set an ambitious target for reducing its carbon footprint, or set a specific percentage goal for diversity hiring. This will allow the company to determine objectively if its goals have been met. The final step is to implement the strategy and assess its results. This requires continuous re-evaluation, as a company's goals may change as the company grows. There are some common pitfalls for companies aiming for sustainability. One of them is the knowledge-action gap: even though many executives set sustainability as one of their core business values, few of them take concrete actions to accomplish sustainability objectives. Another is known as the compliance-competitiveness gap. While improving sustainability metrics can make a company more competitive in the market, these goals should not be confused with the mandatory compliance requirements that a company must adhere to. While sustainability is desirable, compliance is mandatory.",
    "Real-World Example: An interesting example of a successful sustainability strategy is Unilever, the parent company of Dove soaps, Axe body spray, Ben & Jerry's Ice Cream, Hellmann's mayonnaise, and many other familiar brands. In 2010, the company implemented the Unilever Sustainable Living Plan, a ten-year blueprint for reducing the environmental impact of its brands while providing a more fair workplace. By the end of Unilever Sustainable Living Plan, the company was able to announce major achievements in improving its environmental footprint as well as the company's bottom line. By working to conserve water and energy, the company was able to save more than 1 billion euros between 2008 and 2018. Moreover, by creating more opportunities for women, Unilever also become the preferred consumer goods employer for graduate students in 50 countries.",
    "How someone can improve their sustainability: Reduce, reuse, and recycle. Cut down on what you throw away. Follow the three R s to conserve natural resources and landfill space. Volunteer. Volunteer for cleanups in your community. You can get involved in protecting your watershed, too. Educate. When you further your own education, you can help others understand the importance and value of our natural resources. Conserve water. The less water you use, the less runoff and wastewater that eventually end up in the ocean. Choose sustainable. Learn how to make smart seafood choices at www.fishwatch.gov. Shop wisely. Buy less plastic and bring a reusable shopping bag. Use long-lasting light bulbs. Energy efficient light bulbs reduce greenhouse gas emissions. Also flip the light switch off when you leave the room! Plant a tree. Trees provide food and oxygen. They help save energy, clean the air, and help combat climate change. Don't send chemicals into our waterways. Choose non-toxic chemicals in the home and office. Bike more. Drive less."
]

prompt_template = f"""
### Instruction:
You are a Question answer bot and will give an Answer based on the below input context and respond with a short answer to the given question.
Use only the information in the below input to answer the question.
It is critical to limit your answers to the question and dont print anything else.
It is critical to limit your answers to 100 words or less.
If you cannot answer the question, respond with "Sorry, I don't know."

### Input:
Context: {{}}
Question: {{}}

### Response:
"""

model = SentenceTransformer("all-MiniLM-L6-v2")
kb_embeddings = model.encode(knowledge_base)
index = faiss.IndexFlatL2(kb_embeddings.shape[1]) # 384
index.add(kb_embeddings)

def rag_answer(question):
    try:
        # Generate embedding for the question
        question_embedding = model.encode([question])

        # Find the most similar text from the knowledge base using FAISS
        _, most_relevant_idx = index.search(question_embedding, 1)
        relevant_chunk = knowledge_base[most_relevant_idx[0][0]]
        # Format our prompt with the question and relevant context using f-strings
        prompt=prompt_template.format(relevant_chunk, question)

        # Get a response from the language model
        result = pg.Completion.create(
            model="Neural-Chat-7B", #"Nous-Hermes-Llama2-13B",
            prompt=prompt
        )
        return result['choices'][0]['text']
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Sorry, something went wrong. Please try again later."

class ccService:
     def create_user(self, info: string) -> None:
         knowledge_base.append(info)
     
     def get_answer(self, question: string) -> string:
        return rag_answer(question)
