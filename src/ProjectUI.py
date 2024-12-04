import pygame
import sys
import os
pygame.init()

"""
VARIABLES!!!!
team1Index         # Left Team Index, 0 is Arizona, 1 is Atlanta, etc.
team2Index         # Right Team Index
yearIndex          # Data Year Index: 0 is 2021, 1, 2022, 3, 2023
dataStructureIndex # Which Data Structure: 0 is RB Tree, 1 is Hashmap
firstDownT1 = 0
firstDownT2 = 0
yardsT1 = 0
yardsT2 = 0
rushAttemptsT1 = 0
rushAttemptsT2 = 0
passesT1 = 0
passesT2 = 0
incompletionsT1 = 0
incompletionsT2 = 0
touchdownsT1 = 0
touchdownsT2 = 0
sacksT1 = 0
sacksT2 = 0
interceptionsT1 = 0
interceptionsT2 = 0
fumblesT1 = 0
fumblesT2 = 0
dateEntered        # Stores the date string entered by the user
nflTeamsID         # 2 Or 3 Letter Team ID's
"""

# Screen Dimensions
screenInfo = pygame.display.Info()
screenWidth = screenInfo.current_w
screenHeight = screenInfo.current_h

# Fullscreen Window
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
pygame.display.set_caption("NFL Team Comparison")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
OTHER_GRAY = (180, 180, 180)

# Fonts
font = pygame.font.Font(None, int(screenHeight * 0.03))  # Font Size Is Dynamic

# Relative File Directories
scriptDir = os.path.dirname(os.path.abspath(__file__))  # Script Directory
projectRoot = os.path.abspath(os.path.join(scriptDir, os.pardir))  # Project Root
resourcesDir = os.path.join(projectRoot, "resources", "images")
vsImagePath = os.path.join(resourcesDir, "Street_Fighter_VS_logo.png")
logosDir = os.path.join(resourcesDir, "NFL Team Logo's")
backgroundDir = os.path.join(resourcesDir, "Background.png")

# Teams, Year, And Data Structures
nflTeamsName = [
    "Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills",
    "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns",
    "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers",
    "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs",
    "Las Vegas Raiders", "Los Angeles Chargers", "Los Angeles Rams", "Miami Dolphins",
    "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants",
    "New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers",
    "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Commanders"
]

nflTeamsID = [
    "ARI", "ATL", "BAL", "BUF",
    "CAR", "CHI", "CIN", "CLE",
    "DAL", "DEN", "DET", "GB",
    "HOU", "IND", "JAX", "KC",
    "LV", "LAC", "LA", "MIA",
    "MIN", "NE", "NO", "NYG",
    "NYJ", "PHI", "PIT", "SF",
    "SEA", "TB", "TEN", "WAS"
]
years = ["2021", "2022", "2023"]
dataStructures = ["Red-Black Tree", "Hashmap"]

# Selection Indices
# Left Team Index, 0 Is Arizona, 1 Is Atlanta, Etc.
team1Index = 0
# Right Team Index
team2Index = 1
# Data Year Index: 0 Is 2021, 1 Is 2022, 2 Is 2023
yearIndex = 0
# Which Data Structure: 0 Is R-B Tree, 1 Is Hashmap
dataStructureIndex = 0

# Vertical Spacing Adjustment
verticalSpacing = int(screenHeight * 0.25)
logoSize = (250, 250)

# Logo Placement
logo1Rect = pygame.Rect(int(screenWidth * 0.1), verticalSpacing, *logoSize)
logo2Rect = pygame.Rect(screenWidth - int(screenWidth * 0.1) - logoSize[0], verticalSpacing, *logoSize)

# Loading VS Symbol
vsImage = pygame.image.load(vsImagePath)
vsImage = pygame.transform.scale(vsImage, (200, 200))  # Scale to 200x200 pixels
vsRect = vsImage.get_rect()
vsRect.center = ((logo1Rect.x + logo1Rect.width + logo2Rect.x) // 2, verticalSpacing + logoSize[1] // 2)

# Scroller Positioning For Team Names
team1TextPos = (logo1Rect.x + logo1Rect.width // 2, logo1Rect.y - int(screenHeight * 0.1))
team2TextPos = (logo2Rect.x + logo2Rect.width // 2, logo2Rect.y - int(screenHeight * 0.1))

# Bottom Scrollers
bottomOptionSpacing = screenHeight - int(screenHeight * 0.1)
yearTextPos = (screenWidth * 0.3, bottomOptionSpacing)
dataStructureTextPos = (screenWidth * 0.7, bottomOptionSpacing)
timeEfficiencyTextPos = (screenWidth * 0.5, bottomOptionSpacing + int(screenHeight * 0.05))

arrowSize = (50, 50)
leftArrowRect1 = pygame.Rect(team1TextPos[0] - 200, team1TextPos[1] - 25, *arrowSize)
rightArrowRect1 = pygame.Rect(team1TextPos[0] + 150, team1TextPos[1] - 25, *arrowSize)
leftArrowRect2 = pygame.Rect(team2TextPos[0] - 200, team2TextPos[1] - 25, *arrowSize)
rightArrowRect2 = pygame.Rect(team2TextPos[0] + 150, team2TextPos[1] - 25, *arrowSize)

# Year And Data Structure Scrollers
leftArrowYear = pygame.Rect(yearTextPos[0] - 120, bottomOptionSpacing - 20, *arrowSize)
rightArrowYear = pygame.Rect(yearTextPos[0] + 80, bottomOptionSpacing - 20, *arrowSize)
leftArrowDS = pygame.Rect(dataStructureTextPos[0] - 200, bottomOptionSpacing - 20, *arrowSize)
rightArrowDS = pygame.Rect(dataStructureTextPos[0] + 150, bottomOptionSpacing - 20, *arrowSize)

# Function That Loads The Teams Logo
def loadTeamLogo(teamName):
    filename = teamName.replace(" ", "_") + ".png"
    path = os.path.join(logosDir, filename)
    try:
        logo = pygame.image.load(path)
        return pygame.transform.scale(logo, logoSize)
    except pygame.error:
        # Edge Case If No Logo
        placeholder = pygame.Surface(logoSize)
        placeholder.fill(GRAY)
        return placeholder

# Load Default Logos
team1Logo = loadTeamLogo(nflTeamsName[team1Index])
team2Logo = loadTeamLogo(nflTeamsName[team2Index])

# Team Stat Variables
firstDownT1 = 0
firstDownT2 = 0
yardsT1 = 0
yardsT2 = 0
rushAttemptsT1 = 0
rushAttemptsT2 = 0
passesT1 = 0
passesT2 = 0
incompletionsT1 = 0
incompletionsT2 = 0
touchdownsT1 = 0
touchdownsT2 = 0
sacksT1 = 0
sacksT2 = 0
interceptionsT1 = 0
interceptionsT2 = 0
fumblesT1 = 0
fumblesT2 = 0

# Retrieve Team Stats Method
def getTeamOneStats(teamName, year):
    return {
        "First Downs": firstDownT1,
        "Yards": yardsT1,
        "Rush Attempts": rushAttemptsT1,
        "Passes": passesT1,
        "Incompletions": incompletionsT1,
        "Touchdowns": touchdownsT1,
        "Sacks": sacksT1,
        "Interceptions": interceptionsT1,
        "Fumbles": fumblesT1
    }

def getTeamTwoStats(teamName, year):
    return {
        "First Downs": firstDownT2,
        "Yards": yardsT2,
        "Rush Attempts": rushAttemptsT2,
        "Passes": passesT2,
        "Incompletions": incompletionsT2,
        "Touchdowns": touchdownsT2,
        "Sacks": sacksT2,
        "Interceptions": interceptionsT2,
        "Fumbles": fumblesT2
    }

# Draw Text Method
def drawText(text, x, y, textColor=WHITE, outlineColor=BLACK, center=True):
    textSurface = font.render(text, True, textColor)
    outlineSurface = font.render(text, True, outlineColor)

    textRect = textSurface.get_rect()
    outlineRect = outlineSurface.get_rect()

    if center:
        textRect.center = (x, y)
        outlineRect.center = (x, y)
    else:
        textRect.topleft = (x, y)
        outlineRect.topleft = (x, y)

    # Draw Text Outline
    offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in offsets:
        screen.blit(outlineSurface, outlineRect.move(dx, dy))

    # Draw Main Text
    screen.blit(textSurface, textRect)

# Draw Arrow Method
def drawArrow(rect, direction, color=WHITE):
    x, y, w, h = rect
    if direction == "left":
        points = [(x + w, y), (x, y + h // 2), (x + w, y + h)]
    elif direction == "right":
        points = [(x, y), (x + w, y + h // 2), (x, y + h)]
    pygame.draw.polygon(screen, color, points)

# Time Variable
timeEfficiency = 0.0

# Date Input Box
inputBox = pygame.Rect(screenWidth // 2 - 100, team1TextPos[1], 200, 40)
colorInactive = GRAY
colorActive = DARK_GRAY
color = colorInactive
active = False
dateInput = ''
dateEntered = ''

# Draw Menu Method
def draw():
    backgroundImage = pygame.image.load(backgroundDir)
    backgroundImage = pygame.transform.scale(backgroundImage, (screenWidth, screenHeight))  # Scale to screen size
    screen.blit(backgroundImage, (0, 0))

    # Team 1 Scroller
    drawArrow(leftArrowRect1, "left")
    drawText(nflTeamsName[team1Index], team1TextPos[0], team1TextPos[1])
    drawArrow(rightArrowRect1, "right")

    # Team 2 Scroller
    drawArrow(leftArrowRect2, "left")
    drawText(nflTeamsName[team2Index], team2TextPos[0], team2TextPos[1])
    drawArrow(rightArrowRect2, "right")

    # Draw Team Logos
    screen.blit(team1Logo, logo1Rect)
    screen.blit(team2Logo, logo2Rect)

    # Draw The VS Image
    screen.blit(vsImage, vsRect)

    # Team Stats
    team1Stats = getTeamOneStats(nflTeamsName[team1Index], years[yearIndex])
    team2Stats = getTeamTwoStats(nflTeamsName[team2Index], years[yearIndex])

    statYStart1 = logo1Rect.y + logoSize[1] + int(screenHeight * 0.03)
    statYStart2 = logo2Rect.y + logoSize[1] + int(screenHeight * 0.03)

    drawText(f"Team 1 Stats:", logo1Rect.x, statYStart1, center=False)
    for i, (key, value) in enumerate(team1Stats.items()):
        drawText(f"{key}: {value}", logo1Rect.x, statYStart1 + (i + 1) * int(screenHeight * 0.03), center=False)

    drawText(f"Team 2 Stats:", logo2Rect.x, statYStart2, center=False)
    for i, (key, value) in enumerate(team2Stats.items()):
        drawText(f"{key}: {value}", logo2Rect.x, statYStart2 + (i + 1) * int(screenHeight * 0.03), center=False)

    # Bottom Selectors
    drawArrow(leftArrowYear, "left")
    drawText(years[yearIndex], yearTextPos[0], bottomOptionSpacing, center=True)
    drawArrow(rightArrowYear, "right")

    drawArrow(leftArrowDS, "left")
    drawText(dataStructures[dataStructureIndex], dataStructureTextPos[0], bottomOptionSpacing, center=True)
    drawArrow(rightArrowDS, "right")

    # Time Efficiency Text
    drawText(f"Efficiency: {timeEfficiency}", timeEfficiencyTextPos[0], timeEfficiencyTextPos[1])

    # Draw Date Box Label
    labelText = "Enter Date M/D/Y:"
    labelSurface = font.render(labelText, True, WHITE)
    labelRect = labelSurface.get_rect(center=(inputBox.x + inputBox.width // 2, inputBox.y - 30))
    screen.blit(labelSurface, labelRect)

    # Draw Date Input Box
    pygame.draw.rect(screen, color, inputBox, 2)
    txtSurface = font.render(dateInput, True, WHITE)
    screen.blit(txtSurface, (inputBox.x + 5, inputBox.y + 5))
    inputBox.w = max(200, txtSurface.get_width() + 10)

# Event Handler
def update(event):
    global team1Index, team2Index, yearIndex, dataStructureIndex, team1Logo, team2Logo, active, dateInput, color

    if event.type == pygame.MOUSEBUTTONDOWN:
        # Team 1 Scroller
        if leftArrowRect1.collidepoint(event.pos):
            team1Index = (team1Index - 1) % len(nflTeamsName)
            team1Logo = loadTeamLogo(nflTeamsName[team1Index])
            if team1Index == team2Index:
                team1Index = (team1Index - 1) % len(nflTeamsName)
                team1Logo = loadTeamLogo(nflTeamsName[team1Index])
        elif rightArrowRect1.collidepoint(event.pos):
            team1Index = (team1Index + 1) % len(nflTeamsName)
            team1Logo = loadTeamLogo(nflTeamsName[team1Index])
            if team1Index == team2Index:
                team1Index = (team1Index + 1) % len(nflTeamsName)
                team1Logo = loadTeamLogo(nflTeamsName[team1Index])

        # Team 2 Scroller
        if leftArrowRect2.collidepoint(event.pos):
            team2Index = (team2Index - 1) % len(nflTeamsName)
            team2Logo = loadTeamLogo(nflTeamsName[team2Index])
            if team2Index == team1Index:
                team2Index = (team2Index - 1) % len(nflTeamsName)
                team2Logo = loadTeamLogo(nflTeamsName[team2Index])
        elif rightArrowRect2.collidepoint(event.pos):
            team2Index = (team2Index + 1) % len(nflTeamsName)
            team2Logo = loadTeamLogo(nflTeamsName[team2Index])
            if team2Index == team1Index:
                team2Index = (team2Index + 1) % len(nflTeamsName)
                team2Logo = loadTeamLogo(nflTeamsName[team2Index])

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

        # If the user clicks the input box
        if inputBox.collidepoint(event.pos):
            active = not active
        else:
            active = False
        color = colorActive if active else colorInactive

    if event.type == pygame.KEYDOWN:
        if active:
            if event.key == pygame.K_RETURN:  # Handle Enter key
                dateEntered = dateInput
                dateInput = ''
            elif event.key == pygame.K_BACKSPACE:
                dateInput = dateInput[:-1]
            else:
                dateInput += event.unicode

# Main Loop
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
