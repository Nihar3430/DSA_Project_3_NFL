import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Get screen dimensions
screenInfo = pygame.display.Info()
screenWidth = screenInfo.current_w
screenHeight = screenInfo.current_h

# Set the window to fullscreen
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
pygame.display.set_caption("NFL Team Comparison")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Fonts
font = pygame.font.Font(None, int(screenHeight * 0.03))  # Font size dynamically based on screen height

# Define project base directory and paths
scriptDir = os.path.dirname(os.path.abspath(__file__))  # Path to the script's directory
projectRoot = os.path.abspath(os.path.join(scriptDir, os.pardir))  # Go up one level to project root
resourcesDir = os.path.join(projectRoot, "resources", "images")
vsImagePath = os.path.join(resourcesDir, "Street_Fighter_VS_logo.png")
logosDir = os.path.join(resourcesDir, "NFL Team Logo's")

# Teams and Options
nflTeams = [
    "Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills",
    "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns",
    "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers",
    "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs",
    "Las Vegas Raiders", "Los Angeles Chargers", "Los Angeles Rams", "Miami Dolphins",
    "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants",
    "New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers",
    "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Commanders"
]
years = ["2021", "2022", "2023"]
dataStructures = ["Red-Black Tree", "Hashmap"]

# Selection indices
team1Index = 0
team2Index = 1
yearIndex = 0
dataStructureIndex = 0

# Adjust vertical spacing
verticalSpacing = int(screenHeight * 0.25)
logoSize = (250, 250)

# Logo dimensions and placement
logo1Rect = pygame.Rect(int(screenWidth * 0.1), verticalSpacing, *logoSize)
logo2Rect = pygame.Rect(screenWidth - int(screenWidth * 0.1) - logoSize[0], verticalSpacing, *logoSize)

# Load "VS" image
vsImage = pygame.image.load(vsImagePath)
vsImage = pygame.transform.scale(vsImage, (200, 200))  # Scale to 200x200 pixels
vsRect = vsImage.get_rect()
vsRect.center = ((logo1Rect.x + logo1Rect.width + logo2Rect.x) // 2, verticalSpacing + logoSize[1] // 2)

# Scroller positions for team names and arrows
team1TextPos = (logo1Rect.x + logo1Rect.width // 2, logo1Rect.y - int(screenHeight * 0.1))
team2TextPos = (logo2Rect.x + logo2Rect.width // 2, logo2Rect.y - int(screenHeight * 0.1))

# Bottom selectors
bottomOptionSpacing = screenHeight - int(screenHeight * 0.1)
yearTextPos = (screenWidth * 0.3, bottomOptionSpacing)
dataStructureTextPos = (screenWidth * 0.7, bottomOptionSpacing)
timeEfficiencyTextPos = (screenWidth * 0.5, bottomOptionSpacing + int(screenHeight * 0.05))

arrowSize = (50, 50)
leftArrowRect1 = pygame.Rect(team1TextPos[0] - 200, team1TextPos[1] - 25, *arrowSize)
rightArrowRect1 = pygame.Rect(team1TextPos[0] + 150, team1TextPos[1] - 25, *arrowSize)
leftArrowRect2 = pygame.Rect(team2TextPos[0] - 200, team2TextPos[1] - 25, *arrowSize)
rightArrowRect2 = pygame.Rect(team2TextPos[0] + 150, team2TextPos[1] - 25, *arrowSize)

# Year and data structure selectors
leftArrowYear = pygame.Rect(yearTextPos[0] - 100, bottomOptionSpacing - 20, *arrowSize)
rightArrowYear = pygame.Rect(yearTextPos[0] + 100, bottomOptionSpacing - 20, *arrowSize)
leftArrowDS = pygame.Rect(dataStructureTextPos[0] - 200, bottomOptionSpacing - 20, *arrowSize)
rightArrowDS = pygame.Rect(dataStructureTextPos[0] + 200, bottomOptionSpacing - 20, *arrowSize)

# Function to load team logo
def loadTeamLogo(teamName):
    """Load the team logo image for the given team."""
    filename = teamName.replace(" ", "_") + ".png"  # Example: "Arizona Cardinals" -> "Arizona_Cardinals.png"
    path = os.path.join(logosDir, filename)
    try:
        logo = pygame.image.load(path)
        return pygame.transform.scale(logo, logoSize)
    except pygame.error:
        # If logo not found, return a placeholder
        placeholder = pygame.Surface(logoSize)
        placeholder.fill(GRAY)
        return placeholder

# Load default team logos
team1Logo = loadTeamLogo(nflTeams[team1Index])
team2Logo = loadTeamLogo(nflTeams[team2Index])

# Placeholder method for team stats
def getTeamStats(teamName, year):
    return {
        "First Downs": "20",
        "Yards": "400",
        "Rush Attempts": "30",
        "Passes": "40",
        "Incompletions": "10",
        "Touchdowns": "4",
        "Sacks": "2",
        "Interceptions": "1",
        "Fumbles": "1"
    }

# Draw text
def drawText(text, x, y, color=BLACK, center=True):
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    if center:
        textRect.center = (x, y)
    else:
        textRect.topleft = (x, y)
    screen.blit(textSurface, textRect)

# Draw arrows
def drawArrow(rect, direction, color=BLACK):
    """Draw an arrow pointing left or right inside the given rect."""
    x, y, w, h = rect
    if direction == "left":
        points = [(x + w, y), (x, y + h // 2), (x + w, y + h)]
    elif direction == "right":
        points = [(x, y), (x + w, y + h // 2), (x, y + h)]
    pygame.draw.polygon(screen, color, points)

# Draw method for rendering the menu
def draw():
    screen.fill(WHITE)

    # Team 1 Scroller
    drawArrow(leftArrowRect1, "left")
    drawText(nflTeams[team1Index], team1TextPos[0], team1TextPos[1])
    drawArrow(rightArrowRect1, "right")

    # Team 2 Scroller
    drawArrow(leftArrowRect2, "left")
    drawText(nflTeams[team2Index], team2TextPos[0], team2TextPos[1])
    drawArrow(rightArrowRect2, "right")

    # Draw team logos
    screen.blit(team1Logo, logo1Rect)
    screen.blit(team2Logo, logo2Rect)

    # Draw the "VS" image
    screen.blit(vsImage, vsRect)

    # Team stats
    team1Stats = getTeamStats(nflTeams[team1Index], years[yearIndex])
    team2Stats = getTeamStats(nflTeams[team2Index], years[yearIndex])

    statYStart1 = logo1Rect.y + logoSize[1] + int(screenHeight * 0.03)
    statYStart2 = logo2Rect.y + logoSize[1] + int(screenHeight * 0.03)

    drawText(f"Team 1 Stats:", logo1Rect.x, statYStart1, center=False)
    for i, (key, value) in enumerate(team1Stats.items()):
        drawText(f"{key}: {value}", logo1Rect.x, statYStart1 + (i + 1) * int(screenHeight * 0.03), center=False)

    drawText(f"Team 2 Stats:", logo2Rect.x, statYStart2, center=False)
    for i, (key, value) in enumerate(team2Stats.items()):
        drawText(f"{key}: {value}", logo2Rect.x, statYStart2 + (i + 1) * int(screenHeight * 0.03), center=False)

    # Bottom selectors
    drawArrow(leftArrowYear, "left")
    drawText(years[yearIndex], yearTextPos[0], bottomOptionSpacing)
    drawArrow(rightArrowYear, "right")

    drawArrow(leftArrowDS, "left")
    drawText(dataStructures[dataStructureIndex], dataStructureTextPos[0], bottomOptionSpacing)
    drawArrow(rightArrowDS, "right")

    # Time Efficiency
    drawText(f"Efficiency: {dataStructures[dataStructureIndex]}", timeEfficiencyTextPos[0], timeEfficiencyTextPos[1])

# Update method for handling events
def update(event):
    global team1Index, team2Index, yearIndex, dataStructureIndex, team1Logo, team2Logo

    if event.type == pygame.MOUSEBUTTONDOWN:
        # Team 1 Scroller
        if leftArrowRect1.collidepoint(event.pos):
            team1Index = (team1Index - 1) % len(nflTeams)
            team1Logo = loadTeamLogo(nflTeams[team1Index])
            if team1Index == team2Index:
                team2Index = (team2Index + 1) % len(nflTeams)
                team2Logo = loadTeamLogo(nflTeams[team2Index])
        elif rightArrowRect1.collidepoint(event.pos):
            team1Index = (team1Index + 1) % len(nflTeams)
            team1Logo = loadTeamLogo(nflTeams[team1Index])
            if team1Index == team2Index:
                team2Index = (team2Index + 1) % len(nflTeams)
                team2Logo = loadTeamLogo(nflTeams[team2Index])

        # Team 2 Scroller
        if leftArrowRect2.collidepoint(event.pos):
            team2Index = (team2Index - 1) % len(nflTeams)
            team2Logo = loadTeamLogo(nflTeams[team2Index])
            if team2Index == team1Index:
                team1Index = (team1Index + 1) % len(nflTeams)
                team1Logo = loadTeamLogo(nflTeams[team1Index])
        elif rightArrowRect2.collidepoint(event.pos):
            team2Index = (team2Index + 1) % len(nflTeams)
            team2Logo = loadTeamLogo(nflTeams[team2Index])
            if team2Index == team1Index:
                team1Index = (team1Index + 1) % len(nflTeams)
                team1Logo = loadTeamLogo(nflTeams[team1Index])

        # Year Selector
        if leftArrowYear.collidepoint(event.pos):
            yearIndex = (yearIndex - 1) % len(years)
        elif rightArrowYear.collidepoint(event.pos):
            yearIndex = (yearIndex + 1) % len(years)

        # Data Structure Selector
        if leftArrowDS.collidepoint(event.pos):
            dataStructureIndex = (dataStructureIndex - 1) % len(dataStructures)
        elif rightArrowDS.collidepoint(event.pos):
            dataStructureIndex = (dataStructureIndex + 1) % len(dataStructures)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        update(event)

    draw()
    pygame.display.flip()

pygame.quit()
sys.exit()
