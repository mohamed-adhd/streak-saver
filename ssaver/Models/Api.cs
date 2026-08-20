using System;

namespace ssaver.Models;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using System.Text;
using ssaver.Models;
public class Api
{
    public async Task<int> send(string username, string repo, string file, string token)
    {
        HttpClient client = new HttpClient();
        var data = new
        {username,repo,file,token};
        string json = JsonSerializer.Serialize(data);
        var content = new StringContent(json,Encoding.UTF8,"application/json");
        
        
        HttpResponseMessage res = await client.PostAsync("https://streak-saver-six.vercel.app/setup", content);        
        string responseBody = await res.Content.ReadAsStringAsync();
        Console.WriteLine(responseBody);
        return 1;

    }
}