#ai.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Learn about the world's top three soccer players - Lionel Messi, Cristiano Ronaldo, and Neymar Jr.">
    <title>World's Top Soccer Players</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            padding: 30px 0;
            background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
            color: white;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            font-size: 2.8rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
            max-width: 600px;
            margin: 0 auto;
        }
        
        .player-card {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 30px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .player-card:hover {
            transform: translateY(-5px);
        }
        
        .player-header {
            padding: 20px;
            color: white;
            display: flex;
            align-items: center;
        }
        
        .player-header.messi {
            background: linear-gradient(to right, #6a11cb, #2575fc);
        }
        
        .player-header.ronaldo {
            background: linear-gradient(to right, #c21500, #ffc500);
        }
        
        .player-header.neymar {
            background: linear-gradient(to right, #0052d4, #4364f7, #6fb1fc);
        }
        
        .player-number {
            font-size: 3rem;
            font-weight: bold;
            margin-right: 15px;
            opacity: 0.8;
        }
        
        h2 {
            font-size: 1.8rem;
            margin: 0;
        }
        
        .player-content {
            padding: 25px;
        }
        
        .player-image {
            width: 100%;
            height: 250px;
            object-fit: cover;
            border-bottom: 4px solid;
        }
        
        .messi-image {
            border-color: #2575fc;
        }
        
        .ronaldo-image {
            border-color: #ffc500;
        }
        
        .neymar-image {
            border-color: #4364f7;
        }
        
        p {
            margin-bottom: 15px;
            font-size: 1.05rem;
        }
        
        .wiki-link {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #2c3e50;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: 500;
            transition: background-color 0.3s;
        }
        
        .wiki-link:hover {
            background-color: #1a252f;
        }
        
        footer {
            text-align: center;
            padding: 20px;
            margin-top: 30px;
            color: #777;
            border-top: 1px solid #ddd;
        }
        
        @media (min-width: 768px) {
            .player-card {
                display: flex;
            }
            
            .player-image-container {
                flex: 0 0 300px;
            }
            
            .player-image {
                height: 100%;
                border-bottom: none;
                border-right: 4px solid;
            }
        }
        
        @media (max-width: 767px) {
            h1 {
                font-size: 2.2rem;
            }
            
            .player-header {
                flex-direction: column;
                text-align: center;
            }
            
            .player-number {
                margin-right: 0;
                margin-bottom: 10px;
            }
        }
    </style>
</head>

<body>
    <header>
        <h1>World's Top Soccer Players</h1>
        <p class="subtitle">Celebrating the exceptional talent and achievements of modern soccer legends</p>
    </header>
    
    <main>
        <article class="player-card">
            <div class="player-image-container">
                <img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22300%22%20height%3D%22250%22%20viewBox%3D%220%200%20300%20250%22%3E%3Crect%20fill%3D%22%236a11cb%22%20width%3D%22300%22%20height%3D%22250%22%2F%3E%3Ctext%20fill%3D%22white%22%20font-family%3D%22Arial%22%20font-size%3D%2220%22%20x%3D%22120%22%20y%3D%22125%22%3ELionel%20Messi%3C%2Ftext%3E%3C%2Fsvg%3E" alt="Lionel Messi" class="player-image messi-image">
            </div>
            
            <div>
                <div class="player-header messi">
                    <div class="player-number">1</div>
                    <h2>Lionel Messi</h2>
                </div>
                
                <div class="player-content">
                    <p>Lionel Andrés Messi, often considered the greatest footballer of all time, is an Argentine professional player who currently plays as a forward for Inter Miami CF and captains the Argentina national team. Born in Rosario, Argentina, Messi relocated to Spain at age 13 to join Barcelona's famed La Masia academy.</p>
                    
                    <p>Messi's career achievements are staggering: a record seven Ballon d'Or awards, a record six European Golden Shoes, and over 750 senior career goals for club and country. He spent most of his career with Barcelona, where he won a club-record 35 trophies, including ten La Liga titles, four UEFA Champions League titles, and seven Copa del Rey titles.</p>
                    
                    <p>Known for his incredible dribbling, vision, and precise finishing, Messi's playing style has evolved from a dynamic winger to a deep-lying forward. His 2012 season stands as one of the most prolific in football history, with 91 goals scored in all competitions. After more than two decades at Barcelona, Messi transferred to Paris Saint-Germain in 2021 before joining Inter Miami in 2023.</p>
                    
                    <p>Internationally, Messi led Argentina to victory in the 2021 Copa América and the 2022 FIFA World Cup, cementing his legacy as one of the sport's true greats.</p>
                    
                    <a href="https://en.wikipedia.org/wiki/Lionel_Messi" class="wiki-link" target="_blank">Learn more on Wikipedia</a>
                </div>
            </div>
        </article>
        
        <article class="player-card">
            <div class="player-image-container">
                <img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22300%22%20height%3D%22250%22%20viewBox%3D%220%200%20300%20250%22%3E%3Crect%20fill%3D%22%23c21500%22%20width%3D%22300%22%20height%3D%22250%22%2F%3E%3Ctext%20fill%3D%22white%22%20font-family%3D%22Arial%22%20font-size%3D%2220%22%20x%3D%2290%22%20y%3D%22125%22%3ECristiano%20Ronaldo%3C%2Ftext%3E%3C%2Fsvg%3E" alt="Cristiano Ronaldo" class="player-image ronaldo-image">
            </div>
            
            <div>
                <div class="player-header ronaldo">
                    <div class="player-number">2</div>
                    <h2>Cristiano Ronaldo</h2>
                </div>
                
                <div class="player-content">
                    <p>Cristiano Ronaldo dos Santos Aveiro is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Often considered one of the greatest players of all time, Ronaldo has won five Ballon d'Or awards and four European Golden Shoes, both records for a European player.</p>
                    
                    <p>Ronaldo began his senior career with Sporting CP before signing with Manchester United in 2003. After winning three Premier League titles, a UEFA Champions League, and his first Ballon d'Or with United, he transferred to Real Madrid in 2009 for a then-record fee. At Madrid, Ronaldo won 15 trophies, including two La Liga titles and four Champions Leagues, and became the club's all-time top scorer.</p>
                    
                    <p>Known for his athleticism, aerial ability, and powerful striking, Ronaldo has scored over 800 official senior career goals—the most by any player in history. After nine years with Madrid, he signed with Juventus in 2018, winning two Serie A titles, before returning to Manchester United in 2021. In 2023, he signed with Al Nassr.</p>
                    
                    <p>With Portugal, Ronaldo has won the 2016 European Championship and the 2019 UEFA Nations League, and he is the all-time top scorer in international football.</p>
                    
                    <a href="https://en.wikipedia.org/wiki/Cristiano_Ronaldo" class="wiki-link" target="_blank">Learn more on Wikipedia</a>
                </div>
            </div>
        </article>
        
        <article class="player-card">
            <div class="player-image-container">
                <img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22300%22%20height%3D%22250%22%20viewBox%3D%220%200%20300%20250%22%3E%3Crect%20fill%3D%22%230052d4%22%20width%3D%22300%22%20height%3D%22250%22%2F%3E%3Ctext%20fill%3D%22white%22%20font-family%3D%22Arial%22%20font-size%3D%2220%22%20x%3D%22110%22%20y%3D%22125%22%3ENeymar%20Jr%3C%2Ftext%3E%3C%2Fsvg%3E" alt="Neymar Jr" class="player-image neymar-image">
            </div>
            
            <div>
                <div class="player-header neymar">
                    <div class="player-number">3</div>
                    <h2>Neymar Jr</h2>
                </div>
                
                <div class="player-content">
                    <p>Neymar da Silva Santos Júnior, known as Neymar Jr., is a Brazilian professional footballer who plays as a forward for Saudi Pro League club Al Hilal and the Brazil national team. Considered one of the best players of his generation, Neymar is renowned for his flamboyant style, dribbling, finishing, and playmaking abilities.</p>
                    
                    <p>Neymar began his career at Santos in Brazil, where he won several awards while still a teenager, including the 2011 South American Footballer of the Year. He moved to Barcelona in 2013, forming a formidable attacking trio with Lionel Messi and Luis Suárez—known as "MSN"—that won the continental treble in the 2014–15 season.</p>
                    
                    <p>In 2017, Neymar transferred to Paris Saint-Germain in a deal worth €222 million, making him the most expensive player ever. At PSG, he won multiple Ligue 1 titles and domestic cups, and helped lead the club to its first Champions League final in 2020. In 2023, he signed with Saudi club Al Hilal.</p>
                    
                    <p>With the Brazilian national team, Neymar is the all-time top scorer, surpassing Pelé's record. He has represented Brazil in three World Cups and won the 2013 FIFA Confederations Cup. Despite injuries hampering some of his tournament appearances, Neymar remains a crucial player for Brazil as they pursue World Cup glory.</p>
                    
                    <p>Beyond his on-field achievements, Neymar is one of the most marketed athletes in the world, with significant endorsement deals and a massive social media following.</p>
                    
                    <a href="https://en.wikipedia.org/wiki/Neymar" class="wiki-link" target="_blank">Learn more on Wikipedia</a>
                </div>
            </div>
        </article>
    </main>
    
    <footer>
        <p>© 2023 World's Top Soccer Players. This page is for educational purposes only.</p>
    </footer>
</body>
</html>