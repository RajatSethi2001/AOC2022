#include <chrono>
#include <iostream>
#include <map>
#include <string>
#include <utility>

std::map<int, std::map<std::string, int>> checkpoints;

void runPrint(int &bestGeodes, std::map<std::string, int> &blueprint, int minutes, int maxMinutes, int oreBots, int ore, int clayBots, int clay, int obsBots, int obs, int geodeBots, int geode, int &maxOre, int &maxClay, int &maxObs) {
    int newMinutes = minutes + 1;

    bool oreBuild = ore >= blueprint["ore"] && oreBots < maxOre;
    bool clayBuild = ore >= blueprint["clay"] && clayBots < maxClay;
    bool obsBuild = ore >= blueprint["obs-1"] && clay >= blueprint["obs-2"] && obsBots < maxObs;
    bool geodeBuild = ore >= blueprint["geode-1"] && obs >= blueprint["geode-2"];

    int newOre = ore + oreBots;
    int newClay = clay + clayBots;
    int newObs = obs + obsBots;
    int newGeode = geode + geodeBots;

    if (newMinutes >= maxMinutes) {
        if (newGeode > bestGeodes) {
            bestGeodes = newGeode;
        }
        return;
    }

    int remainder = maxMinutes - newMinutes;
    int maxPossible = newGeode + (remainder * geodeBots) + (remainder * (remainder + 1)) / 2;
    if (maxPossible <= bestGeodes) {
        return;
    }

    if (oreBots <= checkpoints[newMinutes]["oreBots"] && newOre <= checkpoints[newMinutes]["ore"] && clayBots <= checkpoints[newMinutes]["clayBots"] && newClay <= checkpoints[newMinutes]["clay"] && obsBots <= checkpoints[newMinutes]["obsBots"] && newObs <= checkpoints[newMinutes]["obs"] && geodeBots <= checkpoints[newMinutes]["geodeBots"] && newGeode <= checkpoints[newMinutes]["geode"]) {
        if (oreBots != checkpoints[newMinutes]["oreBots"] || newOre != checkpoints[newMinutes]["ore"] || clayBots != checkpoints[newMinutes]["clayBots"] || newClay != checkpoints[newMinutes]["clay"] || obsBots != checkpoints[newMinutes]["obsBots"] || newObs != checkpoints[newMinutes]["obs"] || geodeBots != checkpoints[newMinutes]["geodeBots"] || newGeode != checkpoints[newMinutes]["geode"]) {
            return;
        }
    }
    
    if (oreBots >= checkpoints[newMinutes]["oreBots"] && newOre >= checkpoints[newMinutes]["ore"] && clayBots >= checkpoints[newMinutes]["clayBots"] && newClay >= checkpoints[newMinutes]["clay"] && obsBots >= checkpoints[newMinutes]["obsBots"] && newObs >= checkpoints[newMinutes]["obs"] && geodeBots >= checkpoints[newMinutes]["geodeBots"] && newGeode >= checkpoints[newMinutes]["geode"]) {
        // std::cout << newMinutes << " " << newGeode << " " << geodeBots << std::endl;
        checkpoints[newMinutes] = {{"oreBots", oreBots}, {"ore", newOre}, {"clayBots", clayBots}, {"clay", newClay}, {"obsBots", obsBots}, {"obs", newObs}, {"geodeBots", geodeBots}, {"geode", newGeode}};
    }

    runPrint(bestGeodes, blueprint, newMinutes, maxMinutes, oreBots, newOre, clayBots, newClay, obsBots, newObs, geodeBots, newGeode, maxOre, maxClay, maxObs);

    if (oreBuild) {
        runPrint(bestGeodes, blueprint, newMinutes, maxMinutes, oreBots + 1, newOre - blueprint["ore"], clayBots, newClay, obsBots, newObs, geodeBots, newGeode, maxOre, maxClay, maxObs);
    }

    if (clayBuild) {
        runPrint(bestGeodes, blueprint, newMinutes, maxMinutes, oreBots, newOre - blueprint["clay"], clayBots + 1, newClay, obsBots, newObs, geodeBots, newGeode, maxOre, maxClay, maxObs);
    }

    if (obsBuild) {
        runPrint(bestGeodes, blueprint, newMinutes, maxMinutes, oreBots, newOre - blueprint["obs-1"], clayBots, newClay - blueprint["obs-2"], obsBots + 1, newObs, geodeBots, newGeode, maxOre, maxClay, maxObs);
    }

    if (geodeBuild) {
        runPrint(bestGeodes, blueprint, newMinutes, maxMinutes, oreBots, newOre - blueprint["geode-1"], clayBots, newClay, obsBots, newObs - blueprint["geode-2"], geodeBots + 1, newGeode, maxOre, maxClay, maxObs);
    }
}

int main() {
    long result = 1;
    int qualitySum = 0;

    int bestGeodes = 0;
    int trueMax = 32;

    int maxOre = 4;
    int maxClay = 15;
    int maxObs = 15;

    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

    std::cout << "Blueprint 1" << std::endl;
    std::map<std::string, int> blueprint1{{"ore", 2}, {"clay", 4}, {"obs-1", 4}, {"obs-2", 15}, {"geode-1", 2}, {"geode-2", 15}};
    for (int i = 1; i < trueMax; i++) {
        checkpoints[i] = {{"oreBots", 0}, {"ore", 0}, {"clayBots", 0}, {"clay", 0}, {"obsBots", 0}, {"obs", 0}, {"geodeBots", 0}, {"geode", 0}};
    }
    for (int maxMinutes=1; maxMinutes <= trueMax; maxMinutes++) {
        std::cout << "Minutes " << maxMinutes << std::endl;
        runPrint(bestGeodes, blueprint1, 0, maxMinutes, 1, 0, 0, 0, 0, 0, 0, 0, maxOre, maxClay, maxObs);
    }
    result = result * bestGeodes;
    qualitySum += 1 * bestGeodes;

    std::cout << "Blueprint 2" << std::endl;
    bestGeodes = 0;
    maxOre = 4;
    maxClay = 12;
    maxObs = 8;
    std::map<std::string, int> blueprint2{{"ore", 4}, {"clay", 4}, {"obs-1", 4}, {"obs-2", 12}, {"geode-1", 3}, {"geode-2", 8}};
    for (int i = 1; i < trueMax; i++) {
        checkpoints[i] = {{"oreBots", 0}, {"ore", 0}, {"clayBots", 0}, {"clay", 0}, {"obsBots", 0}, {"obs", 0}, {"geodeBots", 0}, {"geode", 0}};
    }
    for (int maxMinutes=1; maxMinutes <= trueMax; maxMinutes++) {
        std::cout << "Minutes " << maxMinutes << std::endl;
        runPrint(bestGeodes, blueprint2, 0, maxMinutes, 1, 0, 0, 0, 0, 0, 0, 0, maxOre, maxClay, maxObs);
    }
    result = result * bestGeodes;
    qualitySum += 2 * bestGeodes;

    std::cout << "Blueprint 3" << std::endl;
    bestGeodes = 0;
    maxOre = 4;
    maxClay = 17;
    maxObs = 16;
    std::map<std::string, int> blueprint3{{"ore", 4}, {"clay", 4}, {"obs-1", 4}, {"obs-2", 17}, {"geode-1", 4}, {"geode-2", 16}};
    for (int i = 1; i < trueMax; i++) {
        checkpoints[i] = {{"oreBots", 0}, {"ore", 0}, {"clayBots", 0}, {"clay", 0}, {"obsBots", 0}, {"obs", 0}, {"geodeBots", 0}, {"geode", 0}};
    }
    for (int maxMinutes=1; maxMinutes <= trueMax; maxMinutes++) {
        std::cout << "Minutes " << maxMinutes << std::endl;
        runPrint(bestGeodes, blueprint3, 0, maxMinutes, 1, 0, 0, 0, 0, 0, 0, 0, maxOre, maxClay, maxObs);
    }
    result = result * bestGeodes;
    qualitySum += 3 * bestGeodes;

    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    std::cout << "Time difference = " << std::chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << "[ms]" << std::endl;

    std::cout << result << std::endl;
    std::cout << qualitySum << std::endl;
    return 0;
}